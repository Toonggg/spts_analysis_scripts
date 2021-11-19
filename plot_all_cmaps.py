import matplotlib as mpl
import matplotlib.pyplot as plt 
import matplotlib.gridspec as gridspec 

def plot_all_maps():
    cpmaps = plt.colormaps()
    num_cmaps = len(cpmaps) 
    print("Number of color maps: %s" % (num_cmaps))
    col_handle = plt.figure(constrained_layout = True, figsize = (30, 30), dpi = 500)
    spec_col = col_handle.add_gridspec(nrows = 13, ncols = 13)

    c_name = 0 
    for c_idx in range(13): 
        for c_idy in range(13): 
            if c_idx == 12 and c_idy == 10:
                break 
            else: 
                sel_map = cpmaps[c_name]
                ax_i = col_handle.add_subplot(spec_col[c_idx,c_idy]) 
                mpl.colorbar.ColorbarBase(ax_i, cmap=plt.get_cmap(sel_map), orientation = 'horizontal')
                ax_i.set_title(sel_map, fontsize = 12,weight = "bold")
                c_name += 1 