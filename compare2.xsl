<?xml version="1.0"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:fo="http://www.w3.org/1999/XSL/Format">
    <xsl:output method="text" omit-xml-declaration="yes" indent="no"/>
    <xsl:template match="/">
        <xsl:text>CITY1,CITY2,STREET,POLICY_ID,CORR_TYPE,CORR_KEY,BUSINESS_PARTNER,CD_VTREF,CD_INSURED_PRSN,CD_FAEDN,CD_DEDUCTN_DATE,CD_CURRENCY,CD_DEDUCTN_AMOUNT,CD_BANK_NAME,CD_CARDTYPE,CD_AC_CARD_NUMBER,CD_CARD_MM_YY,CD_PYMNT_YEAR,CD_PYMNT_COUNT,CD_PAYMENT_MODE&#xa;</xsl:text>
        <xsl:for-each select="//XXXXXCY/XXXXXE_POLICY_S/XXXXX_PREM/XXXXXXXXXPREM_S/XXXXX_PREM">
            <xsl:value-of select=
            "concat(
            ../../../../../XXXXX_ADRESS/CITY1,',',
            ../../../../../XXXXX_ADRESS/CITY2,',',
            ../../../../../XXXXXADRESS/STREET,',',
            ../../../../../XXXXX_HEAD/XXXXX_TAGS/XXXXX_ID,',',
            ../../../../../XXXXX_KEY/CORR_TYPE,',',
            ../../../../../XXXXX_KEY/CORR_KEY,',',
            ../../../../../XXXXX_KEY/XXXXX_PARTNER,',',
            XXXXX_COUNT,',' ,
            XXXXX_MODE, '&#xa;')"/>
        </xsl:for-each>
    </xsl:template>
</xsl:stylesheet>

