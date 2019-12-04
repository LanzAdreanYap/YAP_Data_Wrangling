import pandas as p
data = {'Box':['Box1','Box1','Box1','Box2','Box2','Box2'],'Dimension':['Length','Width','Height','Length','Width','Height'],'Value':[6,4,2,5,3,4]}
messybox = p.DataFrame(data, columns = ['Box','Dimension','Value'])

tidybox = messybox.pivot_table(index = 'Box', columns = 'Dimension', values = 'Value').reset_index()
tidybox['Volume'] = tidybox.Length*tidybox.Width*tidybox.Height