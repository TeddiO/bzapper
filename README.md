# bzapper
Essentially a generic zipping system that allows for zipping each individual file within a directory, while maintaining structure and not dumping it into one central archive.

This is designed to solve a problem that (without bash) you typically cannot put files into it's own individual archive with current solutions. This is for scenarios such as Fast Download with the Source Engine
(think Garry's Mod / CSS) where each file is it's own individual request when being downloaded. 

This can be used as a class (whatever = Bzapper()) or you can just call it directly (python3 bzapper.py <location>).
