from mdutils.mdutils import MdUtils

mdFile = MdUtils(file_name='/Users/mac20/Documents/Obsidian/Notes/Journal/Example_Markdown')
mdFile.new_paragraph("---\ntype:journal\ndate:date")

mdFile.create_md_file()