import gradio as gr
from protein_path import protein_path



finder = protein_path()

def find_path(p1, p2):
    paths = finder.shortest_path(p1, p2)
    if len(paths) == 0:
        return 'None'
    else:
        res = ''
        for path in paths:
            for i in range(len(path) - 1):
                res += f'{path[i]} -> '
            res += path[-1]
        return res


demo = gr.Interface(
    title='Demo of a Protein Path Finder',
    fn=find_path,
    inputs=[gr.Textbox(label="Protein 1"), gr.Textbox(label="Protein 2")],
    outputs=[gr.Textbox(label="Protein Path")]
)

demo.launch()