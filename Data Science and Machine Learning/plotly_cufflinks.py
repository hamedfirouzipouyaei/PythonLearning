import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from plotly.offline import plot, iplot
import plotly.offline as pyo
import cufflinks as cf

# Initialize cufflinks for offline use
cf.go_offline()

# Sample DataFrame  
df = pd.DataFrame(np.random.randn(100, 4), columns='A B C D'.split())
df2 = pd.DataFrame({'Category': ['A', 'B', 'C', 'D'],
                   'Values': [10, 20, 30, 40]})

# This will likely still cause the color parsing error we saw before
try:
    df.iplot()
    plt.show()
except Exception as e:
    print(f"Error with iplot(): {e}")
    print("\nUsing modern Plotly instead:")
    
    # Modern alternative
    fig = px.line(df, title="Using Plotly Express instead")
    plot(fig, filename='modern_plot.html', auto_open=True)