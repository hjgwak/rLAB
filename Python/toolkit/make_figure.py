__author__ = 'yihwan'

import numpy, sys, os
import scipy.cluster.hierarchy as sch
import scipy.spatial.distance as dist
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

def clean_axis(ax):
        ax.get_xaxis().set_ticks([])
        ax.get_yaxis().set_ticks([])
        for sp in ax.spines.values():
            sp.set_visible(False)

def remove_col_under_tol(matrix, row_dic, col_dic, tol):

    remove_list = []
    tol=float(tol)
    for col_key in col_dic:
        i_col   = col_dic[col_key]
        flag=True
        for row_key in row_dic:
            i_row   = row_dic[row_key]
            if matrix[i_row][i_col] > tol:
                flag=False
        if flag:
            remove_list.append('')
            remove_list[-1]=col_key

    for remove_key in remove_list:
        i_col   = col_dic[remove_key]
        for row_key in row_dic:
            i_row   = row_dic[row_key]
            result_matrix[i_row].pop(i_col)
        col_dic.pop(remove_key)
        for k in col_dic:
            if col_dic[k] > i_col:
                col_dic[k] = col_dic[k]-1

    return (matrix, row_dic, col_dic)

def convert_to_log_scale_matrix(matrix):

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                matrix[i][j] = -3
                continue
            matrix[i][j]    = numpy.log10(float(matrix[i][j]))

    return matrix

def make_heatmap_png(data_matrix, colLabel_list, rowLabel_list,\
                     isRowClustering, isColClustering, ratio, fontSize, outputPATH):

    colOrder    = [i for i in range(len(data_matrix[0]))]
    rowOrder    = [j for j in range(len(data_matrix))]
    data_matrix = numpy.array(data_matrix)
    fig         = plt.figure()
    if ratio == -1:
        figRatio    = len(rowLabel_list)/float(len(colLabel_list))
    else:
        figRatio    = ratio
    if figRatio >= 1:
        figWidth    = 50.0/figRatio
    else:
        figWidth    = 50
    figHeight    = figWidth*figRatio
    fig.set_size_inches(figWidth,figHeight)
    heatmapGS   = gridspec.GridSpec(2,2,wspace=0.0,hspace=0.0,width_ratios=[10,figWidth],height_ratios=[10,figHeight])

    #clustering
    clusterMethod       = 'average'
    if isRowClustering:
        #row clustering and dendrogram
        rowDendro_ax        = fig.add_subplot(heatmapGS[1,0])
        rowPairwiseDist     = dist.squareform(dist.pdist(data_matrix), 'euclidean')
        rowCluster          = sch.linkage(rowPairwiseDist, method=clusterMethod)
        sch.set_link_color_palette(['black'])
        row_dendro          = sch.dendrogram(rowCluster, color_threshold=numpy.inf, orientation='right')
        rowOrder            = row_dendro['leaves']
        clean_axis(rowDendro_ax)
        data_matrix = data_matrix[rowOrder, :]

    if isColClustering:
        #column clustering and dendrogram
        colDendro_ax        = fig.add_subplot(heatmapGS[0,1])
        colPairwiseDist     = dist.squareform(dist.pdist(numpy.transpose(data_matrix)), 'euclidean')
        colCluster          = sch.linkage(colPairwiseDist, method=clusterMethod)
        sch.set_link_color_palette(['black'])
        col_dendro          = sch.dendrogram(colCluster, color_threshold=numpy.inf)
        colOrder            = col_dendro['leaves']
        clean_axis(colDendro_ax)
        data_matrix = data_matrix[:, colOrder]





    #depict heatmap
    ax          = fig.add_subplot(heatmapGS[1,1])
    heatmap     = ax.imshow(data_matrix, cmap=plt.cm.PuBuGn,interpolation='nearest',aspect='auto',origin='lower', alpha=1)
    clean_axis(ax)

    #tick and labels
    x_index     = numpy.arange(data_matrix.shape[1])
    y_index     = numpy.arange(data_matrix.shape[0])
    ax.yaxis.tick_left()
    ax.set_xticks(x_index, minor=False)
    ax.set_yticks(y_index, minor=False)
    ax.yaxis.set_ticks_position('right')
    ax.set_xticklabels([colLabel_list[i] for i in colOrder], rotation=90, minor=False)
    if rowLabel_list!=[]:
        ax.set_yticklabels([rowLabel_list[i] for i in rowOrder], minor=False)
    if fontSize == -1:
        ylabelsize = 36
        xlabelsize = ylabelsize*len(rowOrder)/float(len(colOrder))
        if figRatio != -1:
            xlabelsize = xlabelsize/figRatio
    else:
        ylabelsize = fontSize
        xlabelsize = ylabelsize*len(rowOrder)/float(len(colOrder))
        if figRatio != -1:
            xlabelsize = xlabelsize/figRatio

    plt.tick_params(axis='x', labelsize=xlabelsize)
    plt.tick_params(axis='y', labelsize=ylabelsize)
    plt.setp(ax.get_xticklines()+ax.get_yticklines(), visible=False)


    #for colorbar
    scale_cbGSSS    = gridspec.GridSpecFromSubplotSpec(1,2,subplot_spec=heatmapGS[0,0],wspace=0.0,hspace=0.0)
    scale_cbAX      = fig.add_subplot(scale_cbGSSS[0,0])
    cBar            = fig.colorbar(heatmap, scale_cbAX, drawedges=False)
    cBar.ax.tick_params(labelsize=ylabelsize)
    cBar.outline.set_linewidth(0)
    cBar.ax.yaxis.set_ticks_position('left')
    plt.setp(cBar.ax.get_yticklines(), visible=False)

    #plt.tight_layout()
    if outputPATH[-1] == '/':
        plt.savefig(outputPATH+"heatmap.png", format='png')
    else:
        plt.savefig(outputPATH+".png", format='png')



def input_preprocessing(inputFile_list, type, delimiter, isColLabel, isRowLabel):

    input_stream    = open(inputFile_list[0], 'r')
    colLen          = int(len(input_stream.readline().split(delimiter)))
    colLabel_list   = ['' for i in range(colLen)]
    rowLabel_list   = []
    inputData       = []

    if type=='matrix':
        input_stream    = open(inputFile_list[0], 'r')
        for line in input_stream:
            line        = line.rstrip('\n').rstrip('\r').rstrip('\t')
            splitLine   = line.split(delimiter)

            if isColLabel:
                colLabel_list   = splitLine
                isColLabel      = False
                continue

            if isRowLabel:
                rowLabel_list.append('')
                rowLabel_list[-1] = splitLine.pop(0)

            inputData.append([])
            for value in splitLine:
                inputData[-1].append(-1)
                inputData[-1][-1] = float(value)

    return (inputData, colLabel_list, rowLabel_list)


def depict_bin_distribution(inputFile, delimiter, isColLabel, isRowLabel, outputPATH):

    data_list, colLabel_list, rowLabel_list =\
        grep_data_matrix_and_label_list(inputFile, delimiter, isColLabel, isRowLabel)

    maxBin, minBin, interval        = grep_proper_min_max_interval(data_list)
    countBin_list, binIndex_list    = count_bin(data_list, minBin, maxBin, interval)
    binProb_list                    = calculate_prob_per_bin(countBin_list)
    colLabel_list                   = fix_colLabel(colLabel_list, data_list)

    plt.style.use('fivethirtyeight')
    fig, ax     = plt.subplots()
    fig.set_size_inches(25,13)

    for i in range(len(data_list)):
        ax.plot(binProb_list[i], label=colLabel_list[i])

    plt.xticks(range(0,len(binProb_list[0])), binIndex_list)
    ax.set_xticklabels(binIndex_list, rotation=90, minor=False)
    lg_handles, lg_labels = ax.get_legend_handles_labels()
    ax.legend(lg_handles, lg_labels, fontsize=20)

    if outputPATH[-1] == '/':
        plt.savefig(outputPATH+"bin.png", format='png')
    else:
        plt.savefig(outputPATH+".png", format='png')

def depict_line_png(inputFile, delimiter, isColLabel, isRowLabel, outputPATH):

    data_list, colLabel_list, rowLabel_list =\
        grep_data_matrix_and_label_list(inputFile, delimiter, isColLabel, isRowLabel)
    colLabel_list                   = fix_colLabel(colLabel_list, data_list)

    plt.style.use('fivethirtyeight')
    fig, ax     = plt.subplots()
    fig.set_size_inches(25,13)

    for i in range(len(data_list)):
        ax.plot(data_list[i], label=colLabel_list[i])

    lg_handles, lg_labels = ax.get_legend_handles_labels()
    ax.legend(lg_handles, lg_labels, fontsize=20)

    if outputPATH[-1] == '/':
        plt.savefig(outputPATH+"line.png", format='png')
    else:
        plt.savefig(outputPATH+".png", format='png')





def grep_data_matrix_and_label_list(inputFile, delimiter, isColLabel, isRowLabel):

    output_data_list    = None
    colLabel_list       = None
    rowLabel_list       = None
    input_stream        = open(inputFile, 'r')

    flag                = True
    for line in input_stream:
        splitLine   = line.rstrip("\n").split(delimiter)
        if flag:
            flag = False
            if isColLabel:
                if isRowLabel:
                    colLabel_list       = splitLine[1:]
                else:
                    colLabel_list       = splitLine
                output_data_list    = [ [] for i in range(len(colLabel_list))]
                continue
            else:
                if isRowLabel:
                    colLabel_list       = [ '' for i in range(len(splitLine)-1)]
                else:
                    colLabel_list       = [ '' for i in range(len(splitLine))]
                output_data_list    = [ [] for i in range(len(colLabel_list))]

        for i in range(len(output_data_list)):
            if len(splitLine) < len(output_data_list):
                for j in range(len(output_data_list)-len(splitLine)):
                    splitLine.append("")
            output_data_list[i].append('')
            if isRowLabel:
                output_data_list[i][-1] = splitLine[i+1]
            else:
                output_data_list[i][-1] = splitLine[i]


    return output_data_list, colLabel_list, rowLabel_list

def grep_proper_min_max_interval(data_list):

    output_maxBin   = -1000000000
    output_minBin   = 1000000000
    output_interval = -1
    for lineVal_list in data_list:
        for eachVal in lineVal_list:
            if eachVal == '':
                continue
            eachVal = float(eachVal)
            if eachVal < output_minBin:
                output_minBin = eachVal
            if eachVal > output_maxBin:
                output_maxBin = eachVal

    output_interval = int((output_maxBin-output_minBin)/50)
    if output_interval < 1:
        output_interval = 1

    return output_maxBin, output_minBin, output_interval

def count_bin(data_list, minBin, maxBin, interval):

    minBin                  = int(minBin)
    maxBin                  = int(maxBin)+1
    output_binIndex_list    = [ i for i in range(minBin, maxBin, interval)]
    output_bin_list         = [ [ 0 for i in range(len(output_binIndex_list))] for j in range(len(data_list))]

    for i in range(len(data_list)):
        for c_val in data_list[i]:
            if c_val == '':
                continue
            c_val   = float(c_val)
            j       = 0
            for binIndex in output_binIndex_list:
                if c_val >= binIndex and c_val < (binIndex+interval):
                    output_bin_list[i][j]   += 1
                    break
                j += 1

    return output_bin_list, output_binIndex_list

def calculate_prob_per_bin(countBin_list):

    output_binProb_list = []

    for bin_list in countBin_list:
        c_binProb_list  = []
        c_binSum        = float(numpy.sum(bin_list))
        for c_bin in bin_list:
            c_prob  = float(c_bin/c_binSum)
            c_binProb_list.append(-1.0)
            c_binProb_list[-1]  = c_prob

        output_binProb_list.append([])
        output_binProb_list[-1] = c_binProb_list

    return output_binProb_list


def fix_colLabel(colLabel_list, data_list):

    for i in range(len(data_list)):
        c_list  = []
        for val in data_list[i]:
            if val == '' or float(val) == -1:
                continue
            c_list.append(-1)
            c_list[-1]  = float(val)

        c_avg           = str(numpy.average(c_list))
        c_stddev        = str(numpy.std(c_list))
        colLabel_list[i] += '( avg: '+c_avg
        colLabel_list[i] += ', std: '+c_stddev+' )'

    return colLabel_list



def init_argv():

    outputPATH      = './'
    inputFile_list  = []
    type            = ''
    fig             = ''
    color           = 'Blues'
    tol             = 0.0

    ratio           = -1
    fontSize        = -1

    delimiter       = '\t'
    isColLabel      = True
    isRowLabel      = False
    isRowClustering = True
    isColClustering = True


    for i in range(len(sys.argv)):
        #global options
        if sys.argv[i] == "-i":
            j=i+1
            while(1):
                if sys.argv[j].startswith('-'):
                    break
                inputFile_list.append(sys.argv[j])
                j+=1
                if j == len(sys.argv):
                    break

        if sys.argv[i] == "-o":
            outputPATH  = sys.argv[i+1]
        if sys.argv[i] == "-type":
            type    = sys.argv[i+1]
        if sys.argv[i] == "-del":
            delimiter    = sys.argv[i+1]
        if sys.argv[i] == "-fig":
            fig     = sys.argv[i+1]

        if sys.argv[i]=="-tol" and len(sys.argv) > i+1:
            tol     = sys.argv[i+1]

        if sys.argv[i]=="-row_clust" and len(sys.argv) > i+1:
            if sys.argv[i+1] == 'T' or sys.argv[i+1] == 'True' or sys.argv[i+1] == 'true':
                isRowClustering = True
            elif sys.argv[i+1] == 'F' or sys.argv[i+1] == 'False' or sys.argv[i+1] == 'false':
                isRowClustering = False
        if sys.argv[i]=="-col_clust" and len(sys.argv) > i+1:
            if sys.argv[i+1] == 'T' or sys.argv[i+1] == 'True' or sys.argv[i+1] == 'true':
                isColClustering = True
            elif sys.argv[i+1] == 'F' or sys.argv[i+1] == 'False' or sys.argv[i+1] == 'false':
                isColClustering = False

        if sys.argv[i] == "-is_col":
            if sys.argv[i+1] == 'T' or sys.argv[i+1] == 'True' or sys.argv[i+1] == 'true':
                isColLabel = True
            elif sys.argv[i+1] == 'F' or sys.argv[i+1] == 'False' or sys.argv[i+1] == 'false':
                isColLabel = False
        if sys.argv[i] == "-is_row":
            if sys.argv[i+1] == 'T' or sys.argv[i+1] == 'True' or sys.argv[i+1] == 'true':
                isRowLabel = True
            elif sys.argv[i+1] == 'F' or sys.argv[i+1] == 'False' or sys.argv[i+1] == 'false':
                isRowLabel = False
        if sys.argv[i] == '-ratio':
            ratio   = float(sys.argv[i+1])
        if sys.argv[i] == '-font':
            fontSize    = float(sys.argv[i+1])

    return outputPATH,inputFile_list,type, fig,color,tol,\
            delimiter,isColLabel,isRowLabel,isRowClustering, isColClustering,\
            ratio, fontSize

if __name__=='__main__':

    outputPATH,inputFile_list,type, fig,color,tol,\
    delimiter,isColLabel,isRowLabel, isRowClustering, isColClustering,\
    ratio, fontSize                                 = init_argv()


    if type == 'matrix':
        (result_matrix, colLabel_list, rowLabel_list) =\
        input_preprocessing(inputFile_list, type, delimiter, isColLabel, isRowLabel)
        make_heatmap_png(result_matrix, colLabel_list, rowLabel_list, isRowClustering, isColClustering, ratio, fontSize, outputPATH)

    if type == 'dist':
        depict_bin_distribution(inputFile_list[0], delimiter, isColLabel, isRowLabel, outputPATH)

    if type == 'line':
        depict_line_png(inputFile_list[0], delimiter, isColLabel, isRowLabel, outputPATH)

