import os
import arxiv
import argparse
from pdfminer.high_level import extract_text


class PaperProducer(object):
    """Produces Papers"""

    def __init__(self, papers_dir="./papers", old_papers_dir="./", new_papers_dir="./"):
        super(PaperProducer, self).__init__()
        self.arxiv_id = None
        self.old_paper_results = None
        self.old_paper_text = None
        self.new_paper_text = None
        self.new_paper = None
        self.papers_dir = papers_dir
        self.old_papers_dir = old_papers_dir
        self.new_papers_dir = new_papers_dir
        self.setup()

    def setup(self):
        """Setup output dirs for PaperProducer"""

        self.make_dir(dir=self.papers_dir)
        self.make_dir(dir=self.old_papers_dir)
        self.make_dir(dir=self.new_papers_dir)

    def make_dir(self, dir):
        """Make directory if it doesn't exist"""

        if not os.path.exists(dir):
            os.makedirs(dir)

    def download_paper(self, arxiv_id):
        """Download PDF of paper with provided ID"""

        self.arxiv_id = arxiv_id
        search = arxiv.Search(id_list=[self.arxiv_id])
        self.old_paper_results = next(search.results())
        self.old_paper_results.download_pdf(
            dirpath=self.old_papers_dir, filename=f"{arxiv_id}.pdf"
        )

    def pdf2text(self):
        """Convert PDF to text"""

        self.old_paper_text = extract_text(
            os.path.join(self.old_papers_dir, f"{arxiv_id}.pdf")
        )

    def produce_paper_text(self):
        """Find and replace keywords according to Mike
        implement core replacement logic in another method"""

        self.new_paper_text = self.old_paper_text

    def format_paper_text(self):
        """Format new paper text to be nice"""

        pass

    def save_new_paper(self):
        """Save new paper"""

        pass

    def produce_paper_from_arxiv_paper(self, arxiv_id):
        """Run all steps to download a paper and use it to produce a new one"""

        self.download_paper(self.arxiv_id)
        self.pdf2text()
        self.produce_paper_text()
        self.format_paper_text()
        self.save_new_paper()


def parse_arguments(parser):
    """Read user arguments"""

    parser.add_argument(
        "--arxiv_id",
        type=str,
        required=True,
        help="arxiv paper ID to use to produce a new paper",
    )

    args = parser.parse_args()

    return args


if __name__ == "__main__":

    # Build arg parser and parse args
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    args = parse_arguments(parser)

    # Initialize paper producer
    paper_producer = PaperProducer()

    # Produce paper from supplied arxiv paper ID
    paper_producer.produce_paper_from_arxiv_paper(arxiv_id=args.arxiv_id)
