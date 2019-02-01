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
    "from xlrd import open_workbook, cellname"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "SPOTIPY_CLIENT_ID = 'CLIENT ID'\n",
    "SPOTIPY_CLIENT_SECRET = 'CLIENT SECRET'"
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
 
   ],
   "source": [
    "new_dict = {}\n",
    "\n",
    "# Program extracting all columns \n",
    "# name in Python \n",
    "import xlrd \n",
    "       ##(\"address of excel file\")## \n",
    "loc = (\"EXCEL FILE ADDRESS\")\n",
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
    "    new_dict[x[0]] = isrc ##saves dict with song identifier and uri as key pairs in dictionary"
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
    "f = open(\"NAME OF FILE\", \"a\")\n",
    "for key, value in new_dict.iteritems():\n",
    "    thing = key.encode(\"utf-8\") + \" - \" + value.encode(\"utf-8\") + \"\\n\" ##formats into \"Artist - Song Name - ISRC\" \n",
    "    f.write(thing)                                                     ##so that pasting them into file is streamlined\n",
    "    \n",
    "f.close()"
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
