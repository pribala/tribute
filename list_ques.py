import webbrowser
import os

def create_List(args):
    # args = input()
    htmlStr = "<ul>\n"
    for item in args:
        htmlStr += "<li>" + str(item) + "</li>\n"
    htmlStr += "</ul>"
    # h = HTML('html', 'htmlStr')
    return htmlStr	
	
def display_List(args):
    # Create or overwrite the output file
    output_file = open('user_list.html', 'w')	
    # Render the content returned by create_List() on the html file
    # rendered_content = page_content.format(
        # list_content=create_List(args))
    rendered_content = create_List(args)	

    # Output the file
    output_file.write(rendered_content)
    output_file.close()

    # open the output file in the browser (in a new tab, if possible)
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)

# listStr=["Cow", "Dog", "Cat"]
listStr=[1,2,3]	
display_List(listStr)
	
