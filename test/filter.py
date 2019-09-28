import unittest
from app import _parse_html_sentences


class Parse_HTML_TestCase(unittest.TestCase):
    def test_parse_html_sentences(self):
        content = """<p><b>Google LLC</b><sup id="cite_ref-10" class="reference"><a 
        href="#cite_note-10">&#91;9&#93;</a></sup> is an American multinational technology company that specializes 
        in Internet-related services and products, which include <a href="/wiki/Online_advertising" title="Online 
        advertising">online advertising technologies</a>, <a href="/wiki/Search_engine" class="mw-redirect" 
        title="Search engine">search engine</a>, <a href="/wiki/Cloud_computing" title="Cloud computing">cloud 
        computing</a>, software, and hardware.</p> """

        sentences = _parse_html_sentences(content)
        true_sentences = ["Google LLC[9] is an American multinational technology company that specializes in "
                          "Internet-related services and products, which include online advertising technologies, "
                          "search engine, cloud computing, software, and hardware"]
        for sentence, true_sentence in zip(sentences, true_sentences):
            self.assertEqual(sentence, true_sentence)


if __name__ == '__main__':
    unittest.main()
