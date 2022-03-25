import os
import glob
import hdf5_getters


def get_stat_filtered_by_years(basedir, stat,ext='.h5') :
    titles = {"tape": [], "vinyl": [], "kassette": [], "cd": [], "mp3": []}
    for root, dirs, files in os.walk(basedir):
        files = glob.glob(os.path.join(root,'*'+ext))
        for f in files:
            try:
                h5 = hdf5_getters.open_h5_file_read(f)
                
                year = hdf5_getters.get_year(h5)
                
                if year < 1926:
                    continue
                elif year < 1947:
                    titles["tape"].append(stat(h5))
                elif year < 1967:
                    titles["vinyl"].append(stat(h5))
                elif year < 1967:
                    titles["kassette"].append(stat(h5))
                elif year < 1967:
                    titles["cd"].append(stat(h5))
                else: 
                    titles["mp3"].append(stat(h5))
                
                h5.close()
                
            except:
                pass
    return titles