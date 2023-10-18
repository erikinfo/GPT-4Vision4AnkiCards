
import os
import subprocess

def extract_convert_save(input_file, pdf_dir="sliced_pdfs", img_dir="sliced_images"):
    # Ensure output directories exist
    if not os.path.exists(pdf_dir):
        os.makedirs(pdf_dir)
    if not os.path.exists(img_dir):
        os.makedirs(img_dir)

    # Get total number of pages in the input PDF
    total_pages = int(subprocess.getoutput(f'pdfinfo {input_file} | grep Pages:').split()[-1])
    print(total_pages)

    # Loop over the pages in increments of 6
    for start_page in range(1, total_pages + 1, 12):
        end_page = start_page + 11
        if end_page > total_pages:
            end_page = total_pages

         # Define the output paths
        pdf_output = os.path.join(pdf_dir, f'output_{start_page}-{end_page}.pdf')
        combined_output = os.path.join(pdf_dir, f'combined_{start_page}-{end_page}.pdf')
        png_output = os.path.join(img_dir, f'output_{start_page}-{end_page}.png')

        # Execute the commands using os.system (which uses shell by default)
        os.system(f'pdftk {input_file} cat {start_page}-{end_page} output {pdf_output}')
        os.system(f'pdfjam --nup "3x4" --landscape "{pdf_output}" --outfile "{combined_output}"')
        os.system(f'convert -density 600 {combined_output} -quality 100 -alpha remove {png_output}')

    return "Processing completed!"

# Calling the function for demonstration (This won't be executed here)
extract_convert_save("input.pdf")
