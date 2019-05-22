import	jinja2 
import  yaml
from	jinja2		import Template, Environment
from	subprocess	import call, Popen, PIPE, STDOUT
from 	os			import path

#template_file = ""

#conf = yaml.load(open('vars.yml').read())


def cleanup(title, minutes):
    """
        removes all of the files created by LaTeX, then moves the original minutes file into the archives.
    """
    call(("rm",
         f"{title}.aux",
         f"{title}.fdb_latexmk",
         f"{title}.fls",
         f"{title}.log",
         f"{title}.toc",
         f"{title}.tex",
        ))

    call(("mv",
          minutes,
          "archives/",))

def rename_texput(outfile):
    call(("mv", "texput.pdf", f"{outfile}.pdf"))

def fill(template_file, outfile, meeting):
    """
        fills a given template with data.
    """
    env = Environment(
        block_start_string		= '\BLOCK{',
        block_end_string		= '}',
        variable_start_string	= '\VAR{',
        variable_end_string		= '}',
        comment_start_string	= '%/*',
        comment_end_string		= '%*/',
        line_comment_prefix		= '%//',
        line_statement_prefix	= '%%',
        trim_blocks 			= True,
        lstrip_blocks			= True,
        autoescape				= False,
        loader					= jinja2.FileSystemLoader("./"),
    )

    template = env.get_template(template_file)

    #etwas = Popen(("pdflatex"), stdout=PIPE, 
    #              stdin=PIPE, stderr=PIPE).communicate(
    #                                                   input=bytes(
    #                                                         template.render(
    #                                                   ), "utf-8"
    #                                             )
    #                                        )
    #rename_texput(outfile)

    open(outfile, "w").write(
        template.render(
            meeting=meeting,
        )
    )

    call(("latexmk", "--pdf", outfile))

if __name__ == "__main__":
    from sys import argv

    #particular = []
    #while len(argv) > 1:
    #    particular.append(argv.pop())
    #if len(particular) is 0:
    #    exit()

    particular = argv[1::]
    TEMPLATE = "template.tex"
    ZINE_TEMPLATE = "zine_template.tex"

    #for each argument
    for minutes in particular:
        if "z" in particular:
            template_file = ZINE_TEMPLATE
        else:
            template_file = TEMPLATE

        meeting = open(minutes).read()
        outfile = f"""{minutes.split(".")[0]}_n.tex"""
        title = outfile.split(".")[0]
        fill(template_file, outfile, meeting)
        cleanup(title, minutes)
