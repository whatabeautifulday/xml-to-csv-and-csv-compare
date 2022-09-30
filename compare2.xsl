<?xml version="1.0"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:fo="http://www.w3.org/1999/XSL/Format">
    <xsl:output method="text" omit-xml-declaration="yes" indent="no"/>
    <xsl:template match="/">
        <xsl:text>CITY1,CITY2,STREEMENT_MODE&#xa;</xsl:text>
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

