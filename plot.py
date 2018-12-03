import plotly
import plotly.plotly as py
import plotly.graph_objs as go
import pandas as pd

def get_label(df):
    a=[]
    b=[]
    c=[]
    for i, v in enumerate(df['path']):
        path = df['path'][i]
        d, e, f = path.split("/")
        h, i, j = f.split("\\")
        activity, subject, trial = j.split("_")
        a.append(activity)
        b.append(subject)
        c.append(trial)
    df['activity'] = a
    df['subject'] = b
    df['trial'] = c
    return df


if __name__ == '__main__':
    path = 'C:/Dataset/RESULT/C8_result.txt'
    df = pd.read_csv(path, skiprows=4, sep=',', header=None, names={'activity': [1], 'subject': [2], 'trial': [3], 'C8': [4]})
    D01 = df[(df['activity'] == 'D01')]
    D02 = df[(df['activity'] == 'D02')]
    D03 = df[(df['activity'] == 'D03')]
    D04 = df[(df['activity'] == 'D04')]
    D05 = df[(df['activity'] == 'D05')]
    D06 = df[(df['activity'] == 'D06')]
    D07 = df[(df['activity'] == 'D07')]
    D08 = df[(df['activity'] == 'D08')]
    D09 = df[(df['activity'] == 'D09')]
    D10 = df[(df['activity'] == 'D10')]
    D11 = df[(df['activity'] == 'D11')]
    D12 = df[(df['activity'] == 'D12')]
    D13 = df[(df['activity'] == 'D13')]
    D14 = df[(df['activity'] == 'D14')]
    D15 = df[(df['activity'] == 'D15')]
    D16 = df[(df['activity'] == 'D16')]
    D17 = df[(df['activity'] == 'D17')]
    D18 = df[(df['activity'] == 'D18')]
    D19 = df[(df['activity'] == 'D19')]
    F01 = df[(df['activity'] == 'F01')]
    F02 = df[(df['activity'] == 'F02')]
    F03 = df[(df['activity'] == 'F03')]
    F04 = df[(df['activity'] == 'F04')]
    F05 = df[(df['activity'] == 'F05')]
    F06 = df[(df['activity'] == 'F06')]
    F07 = df[(df['activity'] == 'F07')]
    F08 = df[(df['activity'] == 'F08')]
    F09 = df[(df['activity'] == 'F09')]
    F10 = df[(df['activity'] == 'F10')]
    F11 = df[(df['activity'] == 'F11')]
    F12 = df[(df['activity'] == 'F12')]
    F13 = df[(df['activity'] == 'F13')]
    F14 = df[(df['activity'] == 'F14')]
    F15 = df[(df['activity'] == 'F15')]

    trace0 = go.Box(y=D01["C8"], name="D01", boxpoints='outliers')
    trace1 = go.Box(y=D02["C8"], name="D02", boxpoints='outliers')
    trace2 = go.Box(
        y=D03["C8"],
        name="D03",
        boxpoints='outliers'
    )
    trace3 = go.Box(
        y=D04["C8"],
        name="D04",
        boxpoints='outliers'
    )
    trace4 = go.Box(
        y=D05["C8"],
        name="D05",
        boxpoints='outliers'
    )
    trace5 = go.Box(
        y=D06["C8"],
        name="D06",
        boxpoints='outliers'
    )
    trace6 = go.Box(
        y=D07["C8"],
        name="D07",
        boxpoints='outliers'
    )
    trace7 = go.Box(
        y=D08["C8"],
        name="D08",
        boxpoints='outliers'
    )
    trace8 = go.Box(
        y=D09["C8"],
        name="D09",
        boxpoints='outliers'
    )
    trace9 = go.Box(
        y=D10["C8"],
        name="D10",
        boxpoints='outliers'
    )
    trace10 = go.Box(
        y=D11["C8"],
        name="D11",
        boxpoints='outliers'
    )
    trace11 = go.Box(
        y=D12["C8"],
        name="D12",
        boxpoints='outliers'
    )
    trace12 = go.Box(
        y=D13["C8"],
        name="D13",
        boxpoints='outliers'
    )
    trace13 = go.Box(
        y=D14["C8"],
        name="D14",
        boxpoints='outliers'
    )
    trace14 = go.Box(
        y=D15["C8"],
        name="D15",
        boxpoints='outliers'
    )
    trace15 = go.Box(
        y=D16["C8"],
        name="D16",
        boxpoints='outliers'
    )
    trace16 = go.Box(
        y=D17["C8"],
        name="D17",
        boxpoints='outliers'
    )
    trace17 = go.Box(
        y=D18["C8"],
        name="D18",
        boxpoints='outliers'
    )
    trace18 = go.Box(
        y=D19["C8"],
        name="D19",
        boxpoints='outliers'
    )
    trace19 = go.Box(
        y=F01["C8"],
        name="F01",
        boxpoints='outliers'
    )
    trace20 = go.Box(
        y=F02["C8"],
        name="F02",
        boxpoints='outliers'
    )
    trace21 = go.Box(
        y=F03["C8"],
        name="F03",
        boxpoints='outliers'
    )
    trace22 = go.Box(
        y=F04["C8"],
        name="F04",
        boxpoints='outliers'
    )
    trace23 = go.Box(
        y=F05["C8"],
        name="F05",
        boxpoints='outliers'
    )
    trace24 = go.Box(
        y=F06["C8"],
        name="F06",
        boxpoints='outliers'
    )
    trace25 = go.Box(
        y=F07["C8"],
        name="F07",
        boxpoints='outliers'
    )
    trace26 = go.Box(
        y=F08["C8"],
        name="F08",
        boxpoints='outliers'
    )
    trace27 = go.Box(
        y=F09["C8"],
        name="F09",
        boxpoints='outliers'
    )
    trace28 = go.Box(
        y=F10["C8"],
        name="F10",
        boxpoints='outliers'
    )
    trace29 = go.Box(
        y=F11["C8"],
        name="F11",
        boxpoints='outliers'
    )
    trace30 = go.Box(
        y=F12["C8"],
        name="F12",
        boxpoints='outliers'
    )
    trace31 = go.Box(
        y=F13["C8"],
        name="F13",
        boxpoints='outliers'
    )
    trace32 = go.Box(
        y=F14["C8"],
        name="F14",
        boxpoints='outliers'
    )
    trace33 = go.Box(
        y=F15["C8"],
        name="F15",
        boxpoints='outliers'
    )

    data = [trace0,trace1,trace2,trace3,trace4,trace5,trace6,trace7,
            trace8, trace9, trace10, trace11, trace12, trace13, trace14, trace15,
            trace16, trace17, trace18, trace19, trace20, trace21, trace22, trace23,
            trace24, trace25, trace26, trace27, trace28, trace29, trace30, trace31,
            trace32, trace33]
    layout = {
        'shapes': [
            # Line Horizontal
            {
                'type': 'line',
                'y0': 100,
                'y1': 100,
            },
        ]
    }

    fig = {
        'data': data,
        'layout': layout,
    }

    py.plot(fig)
