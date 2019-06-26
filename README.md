<h1>Viewer Part </h1>
The viewer part work with the viewer Mirador. This viewer asks to have only IIIF manifest so you have multiple possibility to create or use this manifests. 

<h2>1°) Manifest for Mirador</h2>

Mirador is complet viewer with all the option integraded directly but he need to have a complet manifest IIIF to work and to follow the complet structure:
[Link to manifest presentation](http://ronallo.com/iiif-workshop/presentation/manifest.html)

![imagemanifest](https://github.com/Corentinfaye/script-manifest/blob/master/Images/conception_manifest.png)

The structure of one manifest part must be always in the same type, you can look the exemple of the codex of the formulae of Angers :
https://fuldig.hs-fulda.de/viewer/rest/iiif/manifests/PPN397372442/manifest/

We can give directly the link of the codex if this  have one manifest by formulae. 
Otherwise, we need to recreate one manifest by formulae and for that, we take the full manifest for base.

<h2>2°) Create all the information for the viewer with one script</h2>

The manifest could be created by one library. But if you don’t have one manifest for the codex, you can create a complete manifest with this website: 
https://digital.bodleian.ox.ac.uk/manifest-editor/

We speak about this website because you have an user interface with all the possibility to create one manifest with all the possibility offers by the IIIF consortium. 
But if you aren’t interested by all this possibility, you can create the manifest directly with the script. You have three possibilty with the script to create 3 type of manifest with one files.

It’s a JSON, each keys must be the name of the corpus and in value you open one list of dictionnary.

The first type is when you know the different images that you need and you have the manifest of the codex who contains the formulae. 
The three keys are :
title : The value must be the complete urn of the formulae.
manifest_link : It’s the link of the manifest with all the picture.
images : It’s a dictionnary who contains all the images. Eache key must be the name of the label of the futur images and the value must be the image id of you need for your formulae

![image_creation_manifest](https://github.com/Corentinfaye/script-manifest/blob/master/Images/default_creation_manifest_image.png)

The second type is when you want to take an manifest who is online, to create this locally.
He need only two keys :
title : The value must be the complete urn of the formulae.
manifest_link : It’s the link of the manifest with all the picture.

![image_copie_manifest](https://github.com/Corentinfaye/script-manifest/blob/master/Images/default_copie_manifest.png)

The third type is when you have only the json images in a IIIF serveur.
The three keys for this possibility:
title : The value must be the complete urn of the formulae.
label : It’s the name of the formulae or the codex
images : It’s a dictionnary who contains all the images. Eache key must be the name of the label of the futur images and the value must be the link who contains the IIIF json of the picture than you need

![image_creation_manifest_image](https://github.com/Corentinfaye/script-manifest/blob/master/Images/default_creation_image.png)

An exemple of the complete view :

![image_complete](https://github.com/Corentinfaye/script-manifest/blob/master/Images/complete_default.png)

<h2>3°) The mapping</h2>

All the information about the mapping is in one Json files Mapping.json. H must follow this structure: Each key must the urn and inside this key, you open one dictionnary, who must have manifest for key and for value the path of the json files

![mapping](https://github.com/Corentinfaye/script-manifest/blob/master/Images/mapping.png)
