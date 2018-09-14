import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()
app.layout = html.Div(children=[
    html.H1('Dash Tutorial'),
    dcc.Graph(id='example',
              figure={
                  'data':[
                      {'x': [1,2,3,4,5], 'y':[10,8,6,4,2], 'type': 'line', 'name': 'boats'},
                      {'x': [1, 2, 3, 4, 5], 'y': [10, 8, 6, 4, 2], 'type': 'line', 'name': 'cars'},
                  ],
                  'layout':{
                      'title':'Basic Dash Example'
                  }
                      })
    ])
# peewee
if __name__=='__main__' :
    app.run_server(debug=True)
