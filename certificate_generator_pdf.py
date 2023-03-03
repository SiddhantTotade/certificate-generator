from python_pptx_text_replacer import TextReplacer
import glob
import tqdm
import os


def clean_up():
    removing_files = "rm -r generated-certificates/* ppt-certificates/*"
    os.system(removing_files)


def generate_certificate():
    replacer = TextReplacer("certificate-templates/certificate_of_completion.pptx", slides='',
                            tables=True, charts=True, textframes=True)
    replacer.replace_text([('{{StudentName}}', 'SIDDHANT TOTADE')])
    replacer.write_presentation_to_file(
        "ppt-certificates/certificate_of_completion.pptx")

    path = "ppt-certificates"
    ext = "pptx"

    files = [f for f in glob.glob(
        path + "/**/*.{}".format(ext), recursive=True)]

    for f in tqdm.tqdm(files):
        command = "unoconv -f pdf \"{}\"".format(f)
        move_file = "mv ppt-certificates/*.pdf generated-certificates"
        os.system(command)
        os.system(move_file)


if __name__ == '__main__':
    clean_up()
    generate_certificate()
