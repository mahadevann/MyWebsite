import pandas as pd
import numpy as np
import matplotlib
import matplotlib.ticker as mtick

matplotlib.use('agg', warn=False, force=True)
from matplotlib import pyplot as plt
import os

from Webtest.settings import STATIC_URL, BASE_DIR


class ProcessFile:
    df = pd.DataFrame
    dcc = pd.DataFrame

    plotimage = ""

    def createDataframe(self, filename):

        # filepath = "/Users/ajit/PycharmProjects/Webtest/templates/blogsite/Millburn.csv"
        fileinp = 'static/Data/' + filename
        filepath = os.path.join(BASE_DIR, fileinp)
        # df = pd.read_csv(filepath, parse_dates=['Sale Date'], error_bad_lines=False)
        df = pd.read_csv(filepath, error_bad_lines=False)
        self.dfinp = df
        return df

    def plotgraph(self, fieldname):
        df = self.dfinp
        df1 = df[(df['Sale Date'] >= '1980-01-01') & (df['Sale Date'] <= '2020-01-01') & (df['Sale Price'] > 99999) & (
                df['Sale Price'] < 20000000)]
        df1['Year'] = pd.to_datetime(df1['Sale Date']).dt.to_period('Y')
        plt.style.use('seaborn-whitegrid')
        dfp = pd.pivot_table(df1, values='Sale Price', index=['Year'], columns=['Municipality'],
                             aggfunc=np.count_nonzero)
        plt.rcParams['figure.figsize'] = 12, 6
        dfp.plot()
        relpath = 'static/images/temp1.png'
        filepath = os.path.join(BASE_DIR, relpath)
        plt.savefig(filepath)
        return relpath

    def getchoices(self):
        p = {}
        dlist = np.arange(1, len(self.dfinp.columns))
        clist = self.dfinp.columns
        for i in range(len(clist) - 3):
            p[dlist[i]] = clist[i]
        t = p.items()
        return t

    def get_columnlist(self):
        self
        return

    def getSalesPriceCount(self, df, type):

        fileinp = 'static/images/Essex/sales'
        fpath = os.path.join(BASE_DIR, fileinp)

        filelists = [file for file in os.listdir(fpath) if file.endswith('price.png')]
        filelistc = [file for file in os.listdir(fpath) if file.endswith('count.png')]

        filelists.sort()
        filelistc.sort()
        return filelists,filelistc

    def boxplotbymuni(self,tid,yfrom):

        df1 = self.df[(self.df['Sale Date'] >= yfrom+'-01-01') & (self.df['Sale Date'] <= '2018-01-01') & (self.df['Sale Price'] > 99999) & (
                self.df['Sale Price'] < 7500000)&(self.df['Municipality'] == int(tid))]
        df1['Code'] = df1['Municipality']
        df1['Sale Date'] = pd.to_datetime(df1['Sale Date'])
        df1['Yr'] = df1['Sale Date'].dt.to_period('Y')
        #dat = pd.merge(df1, self.dcc, on=['Code'])

        #f1 = dat[(dat['Code'] == int(tid)) & (dat['Sale Date'] >= '2000-01-01')]
        d1 = df1.pivot(columns='Yr', values='Sale Price')
        plt.figure(figsize=(18, 7))
        plt.xlabel('Year',fontsize=16)
        plt.ylabel('Sale Price',fontsize=16)
        title = 'Sale price of houses in ' + self.dcc[self.dcc['Code']==int(tid)].iloc[0,0]
        title = title + ', From Year : ' + yfrom
        plt.title(title, fontsize=20)
        d1.boxplot()
        fmt = '${x:,.0f}'
        tick = mtick.StrMethodFormatter(fmt)
        plt.gca().yaxis.set_major_formatter(tick)
        plt.ylim((25, 5000000))
        relpath = 'static/images/temp1.png'
        filepath = os.path.join(BASE_DIR, relpath)
        plt.savefig(filepath)
        return relpath
