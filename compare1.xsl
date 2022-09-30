<?xml version="1.0" encoding="utf-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
<xsl:output method="text" encoding="utf-8"/>
<xsl:template match="/">
          <xsl:text>CITY1,CITY2,STREET,XXXXX_ID,XXXXX_TYPE,XXXXX_KEY,XXXXX_PARTNER&#xa;</xsl:text>

<xsl:for-each select="//XXX_DATA">


<xsl:value-of select="XXXX_ADRESS/CITY1"/><xsl:text>,</xsl:text>
<xsl:value-of select="XXXX_ADRESS/CITY2"/><xsl:text>,</xsl:text>
<xsl:value-of select="XXXX_ADRESS/STREET"/><xsl:text>,</xsl:text>
<xsl:value-of select="XXXX_HEAD/XXXX_TAGS/XXXX_ID"/><xsl:text>,</xsl:text>
<xsl:value-of select="XXXX_KEY/XXXX_TYPE"/><xsl:text>,</xsl:text>
<xsl:value-of select="XXXX_KEY/XXXX_KEY"/><xsl:text>,</xsl:text>
<xsl:value-of select="XXXX_KEY/XXXXX_PARTNER"/>



<xsl:text>
</xsl:text>




</xsl:for-each>
</xsl:template>
</xsl:stylesheet>
