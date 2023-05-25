import os
import matplotlib.pyplot as plt
from posydon.utils.common_functions import PATH_TO_POSYDON
from posydon.visualization.plot_defaults import DEFAULT_LABELS

plt.style.use(os.path.join(PATH_TO_POSYDON, "posydon/visualization/posydon.mplstyle"))

def plot_merger_efficiency(met, merger_efficiency, show=True, path=None, Zsun=0.0142):
    title = r'Merger efficiency'
    plt.figure()
    plt.title(title)
    plt.plot(met/Zsun, merger_efficiency)
    plt.yscale('log')
    plt.xscale('log')
    plt.xlabel(r'$Z/Z_\odot$')
    plt.ylabel(r'\#DCOs [$M_\odot^{-1}$]')
    if path:
        plt.savefig(path)
    if show:
        plt.show()

def plot_merger_rate_density(z, rate_density, zmax=10., show=True, path=None):
    title = r'Merger rate density'
    plt.figure()
    plt.title(title)
    plt.plot(z[z<zmax], rate_density[z<zmax])
    plt.yscale('log')
    plt.ylabel(r'$\mathcal{R}_\mathrm{BBH}\,[\mathrm{Gpc}^{-3}\,\mathrm{yr}^{-1}]$')
    plt.xlabel(r'$z$')
    if path:
        plt.savefig(path)
    if show:
        plt.show()

def plot_hist_dco_properties(x, df_intrinsic=None, df_detectable=None,
                             show=True, path=None, alpha=0.5,
                             range=None, bins=20, ylog=False):
    if df_intrinsic is not None and df_detectable is not None:
        title = r'Intrinsic vs. detectable (dashed) population'
    elif df_intrinsic is not None:
        title = r'Intrinsic population'
    elif f_detectable is not None:
        title = r'Detectable population'
    else:
        raise ValueError('You should provide either an intrinsic or a '
                         'detectable population.')

    colors = ['tab:blue', 'tab:orange', 'tab:green', 'tab:red', 'tab:purple']
    plt.figure()
    plt.title(title)
    if df_intrinsic is not None:
        if isinstance(x, str):
            plt.hist(df_intrinsic[x], weights=df_intrinsic['weight'], color=colors[0],
                     alpha=alpha, density=True, range=range, bins=bins)
        elif isinstance(x, list):
            for i, x_i in enumerate(x):
                if "S1" in x_i:
                    label = 'S1'
                elif "S2" in x_i:
                    label = 'S2'
                else:
                    label = x_i
                plt.hist(df_intrinsic[x_i], weights=df_intrinsic['weight'],
                         color=colors[i], label=label,
                         alpha=alpha, density=True, range=range, bins=bins)
    if df_detectable is not None:
        if isinstance(x, str):
            plt.hist(df_detectable[x], weights=df_detectable['weight'],
                     color=colors[0],
                     histtype=u'step', linestyle='--',
                     alpha=alpha, density=True, range=range, bins=bins)
        elif isinstance(x, list):
            for i, x_i in enumerate(x):
                if "S1" in x_i:
                    label = 'S1'
                elif "S2" in x_i:
                    label = 'S2'
                else:
                    label = x_i
                plt.hist(df_detectable[x_i], weights=df_detectable['weight'],
                         color=colors[i], label=label,
                         histtype=u'step', linestyle='--',
                         alpha=alpha, density=True, range=range, bins=bins)
    if ylog:
        plt.yscale('log')
    plt.ylabel(r'PDF')
    try:
        if isinstance(x, str):
            plt.xlabel(DEFAULT_LABELS[x])
        else:
            plt.xlabel(DEFAULT_LABELS[x[0]])
    except:
        if isinstance(x, str):
            plt.xlabel(x)
        else:
            plt.xlabel(x[0])
    if isinstance(x, list):
        plt.legend(loc=1)
    if path:
        plt.savefig(path)
    if show:
        plt.show()