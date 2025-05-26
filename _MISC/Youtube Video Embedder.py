import webbrowser


def generate_html(youtube_link):
    link_id = youtube_link.split("=")[1]
    html_code = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Embedded YouTube Video</title>
    </head>
    <body>

        <h1>My Embedded YouTube Video</h1>

        <iframe width="560" height="315" src="https://www.youtube.com/embed/{link_id}" frameborder="0" allowfullscreen></iframe>

    </body>
    </html>
    """
    return html_code


def save_html(html_code, filename='embedded_video.html'):
    with open(filename, 'w') as file:
        file.write(html_code)


def main():
    youtube_link = input("Enter the YouTube video link: ")

    # Validate the link (you can add more sophisticated validation if needed)
    if "youtube.com" not in youtube_link:
        print("Invalid YouTube link. Please enter a valid link.")
        return

    html_code = generate_html(youtube_link)
    save_html(html_code)

    # Open the HTML file in a new browser tab
    webbrowser.open_new_tab('embedded_video.html')


if __name__ == "__main__":
    main()