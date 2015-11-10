__author__ = 'yihwan'

import sys, time, os, resource, datetime

def print_USAGE():
    print("\nUSAGE:")
    print("python save_log.py <command>")
    print("\nprint input command which is used,")
    print("      running time of your command and")
    print("      maximum memory hit while running")
    print("==================================================================================")
    print("ex)")
    print("input command:       \t<command>")
    print('maximum memory usage:\t102233')
    print('running time(hour):  \t13.34\n')
    print('When : Sat Nov 26 19:59:23 2011')

if __name__=='__main__':

    flag            = True

    try:
        if sys.argv[1] == '-h' or sys.argv[1] == '--h':
            print_USAGE()
            flag=False

    except IndexError:
        print("\nERROR: improper command, check your command\n")
        print_USAGE()

    except Exception as e:
        print('\n\nError with:\n'+str(e)+'\n')

    else:
        if flag:
            start_time  = time.time()

            input_command = ' '.join(sys.argv[1:])
            os.system(input_command)
            maxMem=(resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss)/1024.0

            end_time = time.time()
            run_time = int(end_time - start_time)
            sec_t = str(run_time % 60)
            run_time /= 60
            min_t = str(run_time % 60)
            run_time /= 60
            hour_t = str(run_time % 24)
            run_time /= 24
            print("\ninput command:       \t"+str(input_command))
            print('maximum memory usage:\t'+str(maxMem))
            print('running time(D:H:M:S):\t'+str(run_time)+':'+hour_t+':'+min_t+':'+sec_t+'\n')
            print('When : ' + datetime.datetime.now().ctime())

