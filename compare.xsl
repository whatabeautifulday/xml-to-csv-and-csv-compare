<?xml version="1.0"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:fo="http://www.w3.org/1999/XSL/Format">
    <xsl:output method="text" omit-xml-declaration="yes" indent="no"/>
    <xsl:template match="/">
        <xsl:text>CITY1,CITY2,STREET,POLICY_ID,CORR_TYPE,CORR_KEY,BUSINESS_PARTNER,CD_VTREF,CD_INSURED_PRSN,CD_DEDUCTN_DATE,CD_CURRENCY,CD_BANK_NAME,CD_FAEDN,CD_CARDTYPE,CD_AC_CARD_NUMBER,CD_CARD_MM_YY,CD_PYMNT_YEAR,CD_PYMNT_COUNT,CD_PAYMENT_MODE&#xa;</xsl:text>
        <xsl:for-each select="//XXX_POLICY/XXXXX_S/XXXXX_PREM/XXXXXX_POLY_PREM_S/XXXXX_PREM">
            <xsl:value-of select=
            "concat(
            ../../../../../XXX_ADRESS/CITY1,',',
            ../../../../../XXX_ADRESS/CITY2,',',
            ../../../../../XXX_ADRESS/STREET,',',
            ../../../../../XXX_HEAD/XXX_TAGS/XXX_ID,',',
            ../../../../../XXXX_KEY/XXX_TYPE,',',
            ../../../../../XXXX_KEY/XXX_KEY,',',
            ../../../../../XXXX_KEY/XXX_PARTNER,',',
            XXX_COUNT,',' ,            
            XXX_MODE,  '&#xa;')"/>
        </xsl:for-each>
    </xsl:template>
</xsl:stylesheet>
