from pysam import VariantFile

def get_header(vcfFile):

    vcf = VariantFile(vcfFile)

    return vcf.header



def get_variants(vcfFile):

    vcf = VariantFile(vcfFile)

    return vcf.fetch()



def extract_vcf_region(vcfFile, region):

    vcf = VariantFile(vcfFile)

    header = vcf.header

    fileString = str(header)

    for rec in vcf.fetch(region['chr'], region['start'], region['end']):

        fileString += (str(rec))

    return fileString
