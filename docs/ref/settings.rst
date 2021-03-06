.. _settings:

***************
Django settings
***************

Below is a list of settings defined by yawd-elfinder. 

.. note::
   You can override all of them in your project's settings file.
   
.. _setting-ELFINDER_JS_URLS:

ELFINDER_JS_URLS
----------------

Default::

   {
      'a_jquery' : '//ajax.googleapis.com/ajax/libs/jquery/1.7.2/jquery.min.js',
      'b_jqueryui' : '//ajax.googleapis.com/ajax/libs/jqueryui/1.8.22/jquery-ui.min.js',
      'c_elfinder' : '%selfinder/js/elfinder.full.js' % settings.STATIC_URL
   }

A dictionary containing the location of javascript files needed by 
yawd-elfinder. 

.. hint::

   Say, for any example, that your project already containts a 
   copy of jquery or query. You could use these settings to avoid loading 
   the google-hosted versions and use your own copies.
   
.. _setting-ELFINDER_CSS_URLS:

ELFINDER_CSS_URLS
-----------------

Default::

   {
    'a_jqueryui' : '//ajax.googleapis.com/ajax/libs/jqueryui/1.8.22/themes/smoothness/jquery-ui.css',
    'b_elfinder' : '%selfinder/css/elfinder.min.css' % settings.STATIC_URL
   }
   
A dictionary containing the css files included by yawd-elfinder.

.. _setting-ELFINDER_LANGUAGES_ROOT_URL:

ELFINDER_LANGUAGES_ROOT_URL
---------------------------

Default:: ``'%selfinder/js/i18n/' % settings.STATIC_URL``

The root url under which elfinder translation files are available. You can
override this in your project's root settings 

.. _setting-ELFINDER_LANGUAGES:

ELFINDER_LANGUAGES
------------------

Default::
   ['ar', 'bg', 'ca', 'cs', 'de', 'el', 'es', 'fa', 'fr', 'hu', 'it', 'jp', 'ko', 'nl', 'no', 'pl', 'pt_BR', 'ru', 'tr', 'zh_CN']
   
A list of the available locales. For each one of these locales, a 
`valid elfinder translation file <https://github.com/Studio-42/elFinder/tree/2.x/js/i18n>`_ 
must exist under the :ref:`setting-ELFINDER_LANGUAGES_ROOT_URL` url. You can
override this setting in your project's main setting file.

.. _setting-ELFINDER_CONNECTOR_OPTION_SETS:

ELFINDER_CONNECTOR_OPTION_SETS
------------------------------

This is a dictionary used by the :class:`elfinder.fields.ElfinderFile` class to define
how the elfinder connector handles files and directories.
Each dictionary key represents a different **set of options**. You can use
this setting to define your own option sets or override the defaults.

.. note::
   
   yawd-elfinder defines two *optionsets*: ``default`` and ``image``; the first
   being used to handle all sorts of files and the latter to allow
   for nothing else than image files in the file manager root directory.
   
Each *optionset* can define one of the following keys:

* ``debug``: indicates if we're on debug mode: ``True`` or ``False``
 
* ``roots``: a list of root directories that elfinder will load on its instatiation. For example, the following will load both `pdfs` and `docs` directories in your media root folder.::
            
      ELFINDER_CONNECTOR_OPTION_SETS = {
         'myoptionset' : {
            'debug' : False,
            'roots' : [
               { 'id' : 'volume1', 'path' : os.path.join(join(settings.MEDIA_ROOT, 'pdfs')) },
               { 'id' : 'volume2', 'path' : os.path.join(join(settings.MEDIA_ROOT, 'docs')) }
            ]
         }
      }
      
Each root can define one of the following keys:

.. _setting-id:

id
++

Required. A unique string representing this root.

.. _setting-driver:

driver
++++++

Required. The volume driver class. yawd-elfinder currently implements the
:class:`elfinder.volumes.filesystem.ElfinderVolumeLocalFileSystem` driver. This can be used to retrieve
files located in your filesystem. Plans exist to implement an FTP driver
in future releases.

.. _setting-path:

path
++++

Required. The path to the root directory.

.. _setting-alias:

alias
+++++

Default: ``''``

A string used by the driver to replace the 
root path and hide it from the end-user. Say you set this to *'My root'*
then elfinder will display *'My Root/docs/document1.doc'* instead of
*'/home/django/project/media/docs/document1.doc'* to the frontend. If not
provided elfinder will just use *'docs/document1.doc'* instead.

.. _setting-startPath:

startPath
+++++++++

Default: ``''``

Open this path on initial request instead of root path.

.. _setting-URL:

URL
+++

Required. The URL corresponding to the root directory. E.g. ``'%sfiles/' % settings.MEDIA_URL``

.. _setting-treeDeep:

treeDeep
++++++++

Default: ``1``

The depth of sub-directories (recursive directory listings) that should 
return per request.

.. _setting-separator:

separator
+++++++++

Default: ``os.sep``

The path separator used by this driver. Normally, you do not want to change
this setting.

.. _setting-tmbPath:

tmbPath
+++++++

Default: ``'.tmb'``

The directory under which auto-generated thumbnails will be placed.

.. _setting-tmbPathMode:

tmbPathMode
+++++++++++

Default: ``0777``

Access rights of the thumbnail directory.

.. _setting-tmbURL:

tmbURL
++++++

Default: ``''``

Thumbnails dir URL. Set this if you're storing thumbnails outside the root directory

.. _setting-tmbSize:

tmbSize
+++++++

Default: ``48``

Thumbnail size (in px)

.. _setting-tmbCrop:

tmbCrop
+++++++

Default: ``True`` 

Whether to crop (scale image to fit) thumbnails or not. Can be ``True`` or ``False``

.. _setting-tmbColor:

tmbBgColor
++++++++++

Default: ``'#ffffff'``

The default thumbnail background color used when the image is not cropped.

.. _setting-copyOverwrite:

copyOverwrite
+++++++++++++

Default: ``True``

Whether on pasting to an existing file should overwrite the original or not.
if `False`` the new file will get a name of the form 
`'{original_name}-{number}.ext}'`.

.. _setting-copyJoin:

copyJoin
++++++++

Default: ``True``

If ``True``, the volume driver will join new and old directory content on 
paste.

.. _setting-onlyMimes:

onlyMimes
+++++++++

Default: ``[]``

A list of the mime types to show for this root. The driver checks if
the file mime type **starts** with values in this lists. Therefore, 
to allow for displaying only images you can use ``['image',]`` and all
files whose mime starts with ``'image'`` (e.g. `'image/png'`, `'image/jpg'` 
etc) will be filtered out.

.. _setting-uploadOverwrite:

uploadOverwrite
+++++++++++++++

Default: ``True``

Used whn uploading files. If ``True``, the old file will be replaced 
with new one. If set to ``False``, the new file will get a name of
the form `'{original_name}-{number}.{ext}'`

.. _setting-uploadAllow:

uploadAllow
+++++++++++

Default: ``['all',]``

A list containing the mime types allowed for upload. Use ``'all'`` for all 
mimetypes. You can also use the first half of a mime type to match
types starting with a certain prefix. E.g. use ``['application',]`` to match 
`'application/pdf'`, `'application/ms-word'` etc.

.. note::

   For more info on how this ssetting is used, 
   see the :ref:`setting-uploadOrder` setting.

.. _setting-uploadDeny:

uploadDeny
++++++++++

Default: ``['all',]``

A list containing the mime types not allowed for upload. Use ``'all'`` for all 
mimetypes. You can also use the first half of a mime type to match
types starting with a certain prefix. E.g. use ``['application',]`` to match 
`'application/pdf'`, `'application/ms-word'` etc.

.. note::

   For more info on how this ssetting is used, 
   see the :ref:`setting-uploadOrder` setting.

.. _setting-uploadOrder:

uploadOrder
+++++++++++

Default: ``['deny', 'allow']``

The order in which to proccess :ref:`setting-uploadAllow` and
:ref:`setting-uploadDeny` options. 

.. note:

   This is modelled after the Apache 
   web server ``Order`` directive, as explained in 
   `the Apache docs <http://httpd.apache.org/docs/2.2/mod/mod_authz_host.html#order>`_

.. _setting-uploadMaxSize:

uploadMaxSize
+++++++++++++

Default: ``'128m'``

The maximum upload file size. 

.. note::
   this corresponds to each uploaded file. It is a hard limit.
 
.. _setting-checkSubFolders:

checkSubfolders
+++++++++++++++

Default: ``True``

If ``True``, each folder will be checked for having child directories. 
When set to ``False``, all folders will be marked as having 
sub-directories and sub-sequent directory listing calls might be generated.
 
.. _setting-copyFrom:

copyFrom
++++++++

Default: ``True``

Whether copying files from this volume to other volumes should be 
allowed or not. ``True`` or ``False``.

.. _setting-copyTo:

copyTo
++++++

Default: ``True``

Whether pasting files originating from other volumes to this volume 
should be allowed or not. ``True`` or ``False``.

.. _setting-disabled:

disabled
++++++++

Default: ``[]``

A list of the commands that should be disabled for this root. For example,
to disallow the creation of new text files and archives in a root 
intented for containing images, you should set this setting to 
``['mkfile', 'archive']``. 

For a list of the available commands, see the 
:class:`elfinder.connector.ElfinderConnector` class.

.. _setting-acceptedName:

acceptedName
++++++++++++

Default: ``r'^[^\.].*'``

Regular expression against which all new file names will be validated.
For example, to allow creating hidden files you could use the value
``r'.*'``.

.. _setting-accessControl:

accessControl
+++++++++++++
 
Default: ``None``

A callable that controls file permissions. If provided, this can override
a file's default permissions. When called, the callable should return 
``True`` if a certain file is given a certain permission, ``False`` if 
not and ``None`` if the standard permission rules should be applied. 
:func:`fs_standard_access` is an example of an accessControl callable
that make dotfiles not readable, not writable, hidden and locked. 

.. _setting-defaults:

defaults
++++++++

Default::
   
   {
      'read' : True,
      'write' : True,
   }
 
Default file permissions. Given a file, these are applied when:

* No :ref:`setting-accessControl` callable is provided, or the callable returns ``None`` for this file
* No :ref:`setting-attributes` rule applies to the file

.. note::
   
   Do not set the ``hidden``and ``locked`` properties here; they would 
   take no effect as the default value for both properties is ``False``. 

.. _setting-attributes:
 
attributes
++++++++++

Default: ``[]``

A list of permissions for specific file name patterns. Each value in the
list must be a dictionary containing at least a ``pattern`` key and one or
more of the ``read``, ``write``, ``locked`` and ``hidden`` properties. 
Any filename will be validated against the ``pattern`` and if a match is 
found, the permission rules will be applied.

For example, to hide and lock the default thumbnails directory (to prevent
viewing and deleting the directory), you could set this to::

   [
      {
         'pattern' : r'\.tmb$',
         'read' : True,
         'write': True,
         'hidden' : True,
         'locked' : True
      },
   ]
   
.. note::

   Given a file, these rules override the :ref:`setting-defaults` permissions,  
   but are ignored if an :ref:`setting-accessControl` callable is set 
   and that callable returns ``True`` or ``False`` for defined properties 
   of the file.

.. _setting-archiveMimes:

archiveMimes
++++++++++++

Default: ``[]``

Allowed archive mimetypes for this root. Leave empty for all available types.

.. _setting-archivers:

archivers
+++++++++

Default: ``{}``

A dictionary with two keys: ``create`` and ``extract``.
The first is used to define classes that generate archive files and the 
latter classes that can open/read archive files.
Use this setting to provide additional archiver implementations, other than
what yawd-elfinder already implements. By default, yawd-elfinder can create 
and read archives having the following mime types

* `application/x-tar` (.tar files)
* `application/x-gzip` (.gzip files)
* `application/x-bzip2` (.bzip files)
* `application/zip` (.zip files)

If you need additional archivers use this setting as follows::

   {
      'create' : { 
         'application/java-archive' :  { 
            'ext' : 'jar',
            'archiver' : MyJarArchiver
          },
          'application/whatever' : {
            'ext' : 'whatever',
            'archiver' : MyWhateverArchiver
          }
      },
      'extract' : {
         'application/java-archive' :  { 
            'ext' : 'jar',
            'archiver' : MyJarReader
          },
          'application/whatever' : {
            'ext' : 'whatever',
            'archiver' : MyWhateverReader
          }
      }
   } 

Create archiver classes (e.g. ``MyJarArchiver`` in the above example) 
must implement the open, add and close methods according to 
Python's built-in :class:`tarfile.TarFile` class.

Extract/read archiver classes (e.g. ``MyJarReader`` in the above example) 
must implement the open, extractall and close methods and operate 
like python's built-in :class:`tarfile.TarFile` class.

For more information see `<http://docs.python.org/library/tarfile.html>`_ and
view yawd-elfinder's :class:`elfinder.utils.archivers.ZipFileArchiver` source code.