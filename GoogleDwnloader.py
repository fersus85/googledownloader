from icrawler.builtin import GoogleImageCrawler


def google_image_dwnloader():
    filters = dict(
        type='photo',
        size='large',
       #  color='black',
       # license='noncomercial, comercial',
       #  date=(2022, 12, 12),
    )

    crawler = GoogleImageCrawler(storage={'root_dir': './img'})
    crawler.crawl(
        keyword='Jenna Ortega', max_num=3, min_size=(2000, 2000), overwrite=True,
        filters=filters
    )


def main():
    google_image_dwnloader()


if __name__ == '__main__':
    main()
