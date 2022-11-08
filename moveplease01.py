#!/usr/bin/env python3
"""RZFeeser | Alta3 Research
   Pushing files around using shutil and os from the standard library"""

# import additional code to complete our task
import shutil
import os

def main():
    """code to move files around"""

    # move into the working directory    
    os.chdir("/home/student/mycode")
    
    # move fileA to a directory
    shutil.move('raynor.obj', 'ceph_storage/')

    xname = input('What is the new name for kerrigan.obj? ')

    shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)


if __name__ == "__main__":
    main()
