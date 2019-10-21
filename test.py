from lxml import etree

import xmlschema


def main():
    schema = xmlschema.XMLSchema('xsd/Request.xsd')

    request_element =  etree.Element('Request')

    proposal_element = etree.Element('Proposal')
    proposal_element.text = 'true'

    request_element.append(proposal_element)

    schema.validate(request_element)


if __name__ == '__main__':
    main()
