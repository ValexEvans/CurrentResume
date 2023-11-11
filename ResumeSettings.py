import jinja2
import pdfkit
from datetime import datetime

my_name = "Valex Jean-Pierre Evans"
my_location = "Orlando, Fl"
my_number = "(407)-280-7573"
my_email = "Valexjpevans@knights.ucf.edu"
my_linkedin = "www.linkedin.com/in/valexjpevans/"
my_github = "github.com/ValexEvans"

today_date = datetime.today().strftime("%d %b, %Y")

context = {'my_name': my_name, 'my_location': my_location, 'my_number': my_number, 'my_email': my_email, 
           'my_linkedin': my_linkedin, 'my_github': my_github,
           'today_date': today_date}

template_loader = jinja2.FileSystemLoader('./')
template_env = jinja2.Environment(loader=template_loader)

html_template = 'ResumeFormat.html'
template = template_env.get_template(html_template)
output_text = template.render(context)

config = pdfkit.configuration(wkhtmltopdf='/usr/local/bin/wkhtmltopdf')
output_pdf = 'CurrentResume.pdf'
pdfkit.from_string(output_text, output_pdf, configuration=config, css='style.css')