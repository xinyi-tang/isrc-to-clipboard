{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "##READ ME##\n",
    "##output: txt file with re-formatted output (1)\n",
    "##very specific function used for string manipulation of identifier for songs + uri => songs + uri\n",
    "##takes correctly formatted string with Spotify URI (2) and returns formatted name for renaming files with ISRC (1)\n",
    "##works on excel files formatted with (1) on column 1\n",
    "##(1) \"artist name - song - URI\"\n",
    "##(2) \"identifier.pdfspotify:track:URI\" //name of song in pdf plus uri when you click \"copy spotify uri\" in spotify"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import sys\n",
    "import spotipy\n",
    "import os\n",
    "from spotipy.oauth2 import SpotifyClientCredentials\n",
    "from xlrd import open_workbook, cellname\n",
    "from xlrd import open_workbook, cellname"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "SPOTIPY_CLIENT_ID = '1eaf33e1f22748dea01e4843efe2f39d'\n",
    "SPOTIPY_CLIENT_SECRET = '9d8e432c2b474faca94b632803d8b5f7'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "client_credentials_manager = SpotifyClientCredentials(client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET)\n",
    "sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "070 Phi - Good Contracts.pdfspotify:track:4vcuBbi9uRXVlMYQ7Ptyyk\n",
      "Agoria - Youre Not Alone.pdfspotify:track:7p9w9UuTQPbzU6dXlSdTwB\n",
      "Anuel Aa - Secreto.pdfspotify:track:5W83ErFkO3aKAIS1WMi6u0\n",
      "Ariana Grande - 7 Rings.pdfspotify:track:14msK75pk3pA33pzPVNtBF\n",
      "Asiahn - Curiosity.pdfspotify:track:7cGzEpKCeLvODoxLFy7ntV\n",
      "Bad Child - Payback.pdfspotify:track:0cxkyGalbYIWXELfgzMqnL\n",
      "Benny Blanco & Calvin Harris - I Found You.pdfspotify:track:3eVuglKxN2sjoIGHAsFAge\n",
      "Billie Eilish - WHEN I WAS OLDER (Music Inspired By The Film ROMA).pdfspotify:track:7tGEAA1f8MydT7eVbbO9Zy\n",
      "Brooks - Limbo - Zoe Moss.pdfspotify:track:6nsxxd4yf7fgSEKPdWGuPb\n",
      "BRWN - So Good.pdfspotify:track:6j7kLm6Hh2GW2c9Bmqdvp2\n",
      "Dean Lewis - Seven Minutes.pdfspotify:track:2BkyYZmU4JuWW2sYi9EzpC\n",
      "DJ Snake - Taki, Taki.pdfspotify:track:4w8niZpiMy6qz1mntFA5uM\n",
      "Fazura - Can’t Forget Me.pdfspotify:track:5mpaksma0ejXr79dPrYwAQ\n",
      "Grey - Want You Back?.pdfspotify:track:0BWx2N8CosqHVKkofenY3R\n",
      "Hozier - Movement.pdfspotify:track:6zmANU5l4qCHQrI5cZhSS2\n",
      "J.S. Ondara - Saying Goodbye.pdfspotify:track:50EByJQioc5CQYbEZEbW9O\n",
      "Jada - Lonely.pdfspotify:track:4hxQsbgMpcp4Y0YSfIVdtx\n",
      "James Blake - Mile High.pdfspotify:track:4cQrSREMqBSvJ8ZzBZjVb8\n",
      "Lady Gaga - Always Remember Us This Way.pdfspotify:track:2rbDhOo9Fh61Bbu23T2qCk\n",
      "Logic - Keanu Reeves.pdfspotify:track:7AnNzyovHm8UEPW5kNM8Fj\n",
      "LOVA - My Name Isnt.pdfspotify:track:0922QmPCA8PuDb19cXKKw3\n",
      "Mabel - Don’t Call Me Up.pdfspotify:track:5WHTFyqSii0lmT9R21abT8\n",
      "Metro Boomin - Space Cadet (feat. Gunna).pdfspotify:track:1fewSx2d5KIZ04wsooEBOz\n",
      "Mustard - Pure Water (ft. Migos).pdfspotify:track:63cd4JkwGgYJrbOizbfmsp\n",
      "Nicole Bus - You.pdfspotify:track:5wUBONclIQRIFrsPzW5TiY\n",
      "Sally - Calculated.pdfspotify:track:4w95mqytGP8C7RgbjHuPsQ\n",
      "Sean Paul - Shot & Wine ft Stefflon Don.pdfspotify:track:1M1k3Sxtf7u8Zj3eIzrJm0\n",
      "Sebastian Yatra - Un Año (feat. Reik).pdfspotify:track:5BDP2tky8oMQJPS33frKVp\n",
      "SHAED - Trampoline.pdfspotify:track:0lsRatBUs9HNIZAmoGABzk\n",
      "Shawn Mendes, Zedd - Lost In Japan Remix.pdfspotify:track:575NJxNUVDqwJGdzBrlLbv\n",
      "Sigrid - Don’t Feel Like Crying.pdfspotify:track:1oLSje4Ot5qRUq8FqYeXOl\n",
      "The Killers - Land Of The Free.pdfspotify:track:489qGxxMxFWIFgtNYFzlAz\n",
      "Yung Gravy - Alley Oop.pdfspotify:track:2GyHLJ238fZx2QkQO9v7nV\n",
      "Yungblud - Loner.pdfspotify:track:5QMmZqzh93EY6gJG4PmzHA\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "{u'070 Phi - Good Contracts': u'QM8RL1900732',\n",
       " u'Agoria - Youre Not Alone': u'FR00Y1800048',\n",
       " u'Anuel Aa - Secreto': u'USXDR1900020',\n",
       " u'Ariana Grande - 7 Rings': u'USUM71900110',\n",
       " u'Asiahn - Curiosity': u'QZEG41801243',\n",
       " u'BRWN - So Good': u'PHUM71800158',\n",
       " u'Bad Child - Payback': u'CAUM71800143',\n",
       " u'Benny Blanco & Calvin Harris - I Found You': u'USUM71822027',\n",
       " u'Billie Eilish - WHEN I WAS OLDER (Music Inspired By The Film ROMA)': u'USUM71900059',\n",
       " u'Brooks - Limbo - Zoe Moss': u'NLDD61800222',\n",
       " u'DJ Snake - Taki, Taki': u'USUG11801723',\n",
       " u'Dean Lewis - Seven Minutes': u'AUUM71800254',\n",
       " u'Fazura - Can\\u2019t Forget Me': u'MYUM71900001',\n",
       " u'Grey - Want You Back?': u'USUM71814737',\n",
       " u'Hozier - Movement': u'USSM11806792',\n",
       " u'J.S. Ondara - Saying Goodbye': u'USUM71810630',\n",
       " u'Jada - Lonely': u'DKUM71800767',\n",
       " u'James Blake - Mile High': u'GBUM71807985',\n",
       " u'LOVA - My Name Isnt': u'SEUM71800784',\n",
       " u'Lady Gaga - Always Remember Us This Way': u'USUM71813195',\n",
       " u'Logic - Keanu Reeves': u'USUM71900414',\n",
       " u'Mabel - Don\\u2019t Call Me Up': u'GBUM71808052',\n",
       " u'Metro Boomin - Space Cadet (feat. Gunna)': u'USUG11802484',\n",
       " u'Mustard - Pure Water (ft. Migos)': u'USUM71823137',\n",
       " u'Nicole Bus - You': u'QMJMT1801926',\n",
       " u'SHAED - Trampoline': u'QZ47A1800201',\n",
       " u'Sally - Calculated': u'NZBJ11800002',\n",
       " u'Sean Paul - Shot & Wine ft Stefflon Don': u'GBUM71808086',\n",
       " u'Sebastian Yatra - Un An\\u0303o (feat. Reik)': u'USUM71821048',\n",
       " u'Shawn Mendes, Zedd - Lost In Japan Remix': u'USUM71813582',\n",
       " u'Sigrid - Don\\u2019t Feel Like Crying': u'GBUM71807541',\n",
       " u'The Killers - Land Of The Free': u'USUM71821044',\n",
       " u'Yung Gravy - Alley Oop': u'USUM71821830',\n",
       " u'Yungblud - Loner': u'USUG11800785'}"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "new_dict_3 = {}\n",
    "\n",
    "# Program extracting all columns \n",
    "# name in Python \n",
    "import xlrd \n",
    "  \n",
    "loc = (\"Desktop/2019-01-24.xls\")\n",
    "  \n",
    "wb = xlrd.open_workbook(loc) \n",
    "sheet = wb.sheet_by_index(0) \n",
    "  \n",
    "# For row 0 and column 0 \n",
    "sheet.cell_value(0, 0) \n",
    "  \n",
    "for i in range(sheet.nrows): \n",
    "    print sheet.cell_value(i,0)\n",
    "    x = sheet.cell_value(i,0).split(\".pdfspotify:track:\")\n",
    "    track = sp.track(x[1])\n",
    "    isrc = track[\"external_ids\"][\"isrc\"]\n",
    "    new_dict_3[x[0]] = isrc\n",
    "    \n",
    "new_dict_3"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [],
   "source": [
    "#write dict into excel\n",
    "      ##(\"name of file\", \"a for append file\")##\n",
    "f = open(\"2019-01-24(isrc).txt\", \"a\")\n",
    "for key, value in new_dict_3.iteritems():\n",
    "    thing = key.encode(\"utf-8\") + \" - \" + value.encode(\"utf-8\") + \"\\n\" ##formats into \"Artist - Song Name - ISRC\" \n",
    "    f.write(thing)                                                     ##so that pasting them into file is streamlined\n",
    "    \n",
    "f.close()\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 2",
   "language": "python",
   "name": "python2"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 2
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython2",
   "version": "2.7.15"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
