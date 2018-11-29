from bokeh.plotting import figure, show, output_notebook, output_file
from bokeh.models import ColumnDataSource, Range1d, LabelSet, Label
from bokeh.palettes import Category20
from sklearn.manifold import TSNE

def word_vecs_tsne_groups(words, word_vecs, groups = None):

    tsne = TSNE(n_components=2, metric='cosine').fit_transform(word_vecs)

    output_notebook()

    p = figure(title="vocab", tools='pan,reset,wheel_zoom,box_zoom,save',
              active_scroll='wheel_zoom', width = 1000, height=700)


    p.title.align = "center"
    p.title.text_font_size = "35px"

    if not groups: 
        groups = [0] * len(words)
        
    palette = Category20[max(3,len(set(groups)))]

    x,y= list(zip(*tsne))

    #markers = ["circle", "square", "*","x","diamond","triangle"]
    pos_colors = [palette[pos] for pos in groups]

    source = ColumnDataSource(data=dict(x=x,
                                        y=y,
                                        words=words,
                                        colors=pos_colors))

    labels = LabelSet(x='x', y='y', text='words', source=source)
    # bokeh.plotting.markers()
    # circle, square, +, *,x,diamond,triangle
    p.scatter(x='x', y='y', size=14, source=source, color='colors')
    p.add_layout(labels)

    show(p,  notebook_handle=True)