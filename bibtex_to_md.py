import os
import bibtexparser
import collections

### utility function ###

def keep_last_and_only(authors_str):
    """
    This function is dedicated to parse authors, it removes all the "and" but the last and and replace them with ", "
    :param str: string with authors
    :return: string with authors with only one "and"
    """

    last_author = authors_str.split(" and ")[-1]

    without_and = authors_str.replace(" and ", ", ")

    str_ok = without_and.replace(", " + last_author, " and " + last_author)

    return str_ok


def get_bibtex_line(filename, ID):
    start_line_number = 0
    end_line_number = 0

    with open(filename, encoding="utf-8") as myFile:
        for num, line in enumerate(myFile, 1):

            # first we look for the beginning line
            if start_line_number == 0:
                if (ID in line) and not ("@String" in line):
                    start_line_number = num
            else:  # after finding the start_line_number we go there
                # the last line contains "}"

                # we are at the next entry we stop here, end_line_number have the goof value
                if "@" in line:
                    assert end_line_number > 0
                    break

                if "}" in line:
                    end_line_number = num
    assert end_line_number > 0
    return start_line_number, end_line_number


def create_bib_link(ID):
    link = bibtex_filename
    start_bib, end_bib = get_bibtex_line(link, ID)

    # bibtex file is one folder upon markdown files
    #link = "../blob/master/" + link
    link += "#L" + str(start_bib) + "-L" + str(end_bib)

    # L66-L73
    return link


def get_md_entry(DB, entry, add_comments=True):
    """
    Generate a markdown line for a specific entry
    :param entry: entry dictionary
    :return: markdown string
    """
    md_str = ""

    if 'url' in entry.keys():
        md_str += "- [**" + entry['title'] + "**](" + entry['url'] + ") "
    else:
        md_str += "- **" + entry['title'] + "**"

    md_str += ", (" + entry['year'] + ")"

    md_str += " by *" + keep_last_and_only(entry['author']) + "*"

    md_str += " [[bib]](" + create_bib_link(entry['ID']) + ") "

    md_str += '\n'

    if add_comments:
        # maybe there is a comment to write
        if entry['ID'].lower() in DB.strings:
            #print("Com : " + entry['ID'])
            md_str += " \n *"
            md_str += DB.strings[entry['ID'].lower()]
            md_str += "* \n"

    return md_str


def get_md(DB, item, key, add_comments):
    """
    :param DB: list of dictionary with bibtex
    :param item: list of keywords to search in the DB
    :param key: key to use to search in the DB author/ID/year/keyword...
    :return: a md string with all entries corresponding to the item and keyword
    """

    all_str = ""

    #list_entry = {}
    list_entry = collections.OrderedDict()

    number_of_entries = len(DB.entries)
    for i in range(number_of_entries):
        if key in DB.entries[i].keys():
            if any(elem in DB.entries[i][key] for elem in item):
                str_md = get_md_entry(DB, DB.entries[i], add_comments)
                list_entry.update({str_md:DB.entries[i]['year']})


    #sorted_tuple_list = sorted(list_entry.items(), reverse=True, key=lambda x: x[1])
    sorted_tuple_list = list_entry.items()
    for elem in sorted_tuple_list:
        all_str += elem[0]

    return all_str


def get_outline(list_classif, filename):
    str_outline = "# Predictive Coding Paper Repository \n"

    str_outline += "This repository provides a list of papers that are interesting or influential about Predictive Coding. If you believe I have missed any papers, please contact me at *beren@millidge.name* or make a pull request with the information about the paper. I will be happy to include it. \n\n"

    str_outline += "## Predictive Coding \n"
    str_outline += "Predictive Coding is a neurophysiologically-grounded theory of perception and learning in the brain. The core idea is that the brain always maintains a prediction of the expected state of the world, and that this prediction is then compared against the true sensory data. Where this prediction is wrong, prediction errors are generated and propagated throughout the brain. The brain's 'task' then is simply to minimize prediction errors. \n \n"
    str_outline += "The key distinction of this theory is that it proposes that prediction-errors, rather than predictions, or direct representation of sense-data is in some sense the core computational primitive in the brain. \n \n"
    str_outline += "Predictive coding originated in studies of ganglion cells in the retina, in light of theories in signal processing, about how it is much more efficient to send only 'different' or 'unpredicted signals' than repeating the whole signal every time -- see delta-encoding. \n \n"
    str_outline += "Predictive coding has several potential neurobiologically plausible process theories proposed for it -- see 'Process Theories' section, although the empirical evidence for precise prediction error minimization in the brain is mixed \n \n"
    str_outline += "Predictive coding has also been extended in several ways. It can be understood as a variational inference algorithm under a Gaussian generative model and variational distribution. It can be setup as an autoencoder (predict your input, or next-state), or else in a supervised learning fashion. \n \n"
    str_outline += "Predictive coding can also be extended to a hierarchical model of multiple predictive coding layers -- as in the brain -- as well as using 'generalised coordinates' which explicitly model the higher order derivatives a state in order to be able to explicitly model dynamical systems. \n \n"
    str_outline += "More recent work has also focused on the relationship between predictive coding and the backpropagation of error algorithm in machine learning where under certain assumptions, predictive coding can approximate this fundamental algorithm in a biologically plausible fashion. Although the exact details and conditions still need to be worked out. \n \n"
    str_outline += "There has also been much exciting work trying to merge predictive coding with machine learning to produce highly performant predictive-coding-inspired architectures. \n \n"
    for item in list_classif:
        str_outline += "- [" + item[0] + "](https://github.com/BerenMillidge/Predictive_Coding_Papers/blob/master/" + filename + "#" \
                       + item[0].replace(" ", "-").lower() + ')\n'

    return str_outline


def get_acknowledgements():
    #str_outline = "\n \n"
    #str_outline += "## Acknowledgements \n \n"
    #str_outline += "Many thanks to @conorheins for his helpful suggestions. \n \n"
    return ""

def get_footnote_string():
    str_outline = "\n \n"
    str_outline += "## Contributing \n \n"
    str_outline += "To contribute, please make pull requests adding entries to the bibtex file.  \n \n The README file was generated from bibtex using the `bibtex_to_md.py` file. \n The keywords to use for each classification ('Classic','Backprop') can be found at the bottom of the .py file. \n"
    str_outline += "\n \n"
    str_outline += "*This code and structure is heavily inspired by https://github.com/optimass/continual_learning_papers.*"
    return str_outline


def generate_md_file(DB, list_classif, key, plot_title_fct, filename, add_comments=True):
    """
    :param DB: list of dictionnary with bibtex
    :param list_classif: list with categories we want to put inside md file
    :param key: key allowing to search in the bibtex dictionary author/ID/year/keyword...
    :param plot_title_fct: function to plot category title
    :param filename: name of the markdown file
    :return: nothing
    """

    all_in_one_str = ""
    all_in_one_str += get_outline(list_classif, filename)

    for item in list_classif:

        str = get_md(DB, item, key, add_comments)

        if str != "":
            all_in_one_str += plot_title_fct(item)
            all_in_one_str += str

    all_in_one_str += get_acknowledgements()
    all_in_one_str += get_footnote_string()

    f = open(filename, "w")
    f.write(all_in_one_str)
    f.close()

if __name__ == '__main__':
    bibtex_filename = "bibtex.bib"
    file_name = 'bibtex.bib'
    with open(file_name) as bibtex_file:
        bibtex_str = bibtex_file.read()

    bib_db = bibtexparser.loads(bibtex_str, parser=bibtexparser.bparser.BibTexParser(ignore_nonstandard_types=False))

    ################################### Create Readme ####################################
    def plot_titles(titles):
        return '\n' + "## " + titles[0] + '\n'

    FEP_list_types = [["Surveys and Tutorials", "survey"],
                ["Classics","classic"],
                ["Neurobiological Process Theories ", "process"],
                ["Relationship to Backpropagation", "backprop"],
                ["PC-inspired machine learning","ml"],
                ["Extensions and Developments","extensions"],
                ["Relationship to FEP", "fep"],
                ]


    generate_md_file(DB=bib_db, list_classif=FEP_list_types, key="keywords", plot_title_fct=plot_titles, filename= "README.md", add_comments=True)
