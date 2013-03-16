makerbot-stuff
==============

A random collection of custom-written objects related to MakerBots

MakerWare Download
------------------

A script to pull all the .debs for makerware 2.0.? from their S3 bucket.
*This script is a temporary hack until MakerBot fixes their repositories*.  Please see makerbot support issues [#100549] [1] and [#102840] [2].  This script will likely become *entirely useless* once these issues are resolved.
[1]: http://support.makerbot.com/requests/100549	"#100549"
[2]: http://support.makerbot.com/requests/102840	"#102840"
<dl>
<dt>MakerWareDownload.py</dt>
<dd>Script to download the debs for MakerWare 2.0.?  Takes three parameters: the version number (ie: 2.0.0), the architecture you want (i386 or amd64) and the version of Ubuntu you want to use it on (ie: precise)
    $ ./MakerWareDownload.py 2.0.1 amd64 precise
</dd>
