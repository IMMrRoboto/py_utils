import pandas as pd
import pickle

def savePickle(dataFrame, pickleName="df_pickle.p"):
    pickle.dump( dataFrame, open( pickleName, "wb" ) )

def changeToNumeric(dataFrame, columnArr):
    for col in columnArr:
        dataFrame[col] = pd.to_numeric(dataFrame[col],errors='coerce')
    return dataFrame

def getQuants(df):
    return df['Loan_Amount_000'].dropna().quantile([.2,.4,.6,.8]).tolist()

def barPlots(dfArr, titlesArr, col, title=''):
    fig, axarr = plt.subplots(nrows=1, ncols=5, sharex='col', sharey='row')

    fig.suptitle(title, fontsize=24, y=1.2)
    
    axarr[0].bar(dfArr[0].As_of_Year, dfArr[0][col])
    axarr[0].set_title(titlesArr[0], fontsize=20,)

    axarr[1].bar(dfArr[1].As_of_Year, dfArr[1][col])
    axarr[1].set_title(titlesArr[1], fontsize=20,)

    axarr[2].bar(dfArr[2].As_of_Year, dfArr[2][col])
    axarr[2].set_title(titlesArr[2], fontsize=20,)

    axarr[3].bar(dfArr[3].As_of_Year, dfArr[3][col])
    axarr[3].set_title(titlesArr[3], fontsize=20,)

    axarr[4].bar(dfArr[4].As_of_Year, dfArr[4][col])
    axarr[4].set_title(titlesArr[4], fontsize=20,)

    fig.set_size_inches(20, 3)

    plt.show()
