import json
import ssl
import os
from glob import glob
import sys
import requests


def create_mapping(args):
    if os.path.isdir(args):
        files = [x for x in glob(args + '/*.json') if os.path.basename(x) != 'Mapping.json']
        path = args
    elif os.path.isfile(args):
        path = os.path.dirname(args)
        files = [args]
    else:
        raise FileNotFoundError('{} must be an existing directory or file.'.format(args))
    d = {}
    existing_mapping = {}
    # Check if there is an existing mapping file in the path
    # If so, it will be extended instead of replaced.
    mapping_file = os.path.join(path, "Mapping.json")
    if os.path.isfile(mapping_file):
        with open(mapping_file) as f:
            existing_mapping = json.load(f)
    # ssl._create_default_https_context = ssl._create_unverified_context

    for file in files:
        with open(file, 'r') as f:
            data_text = json.load(f)
        for manifests in data_text:
            for manifest in data_text[manifests]:
                dict_manifest = create_manifest(manifest)
                if dict_manifest is False:
                    continue
                d['manifest:' + manifest["title"]] = {"manifest": os.path.join(manifests, manifest["title"] + ".json"),
                                                      'title': manifest['codex_name']}
                os.makedirs(os.path.join(path, manifests), exist_ok=True)
                with open(os.path.join(path, manifests, manifest["title"] + ".json"), 'w') as f:
                    json.dump(dict_manifest, f, ensure_ascii=False, indent='\t')

    existing_mapping.update(d)

    with open(os.path.join(path, "Mapping.json"), "w")as f:
        json.dump(existing_mapping, f, ensure_ascii=False, indent='\t')


def create_manifest(manifest):
    filename = manifest["title"]
    # creation of manifest directly by the script
    if "manifest_link" not in manifest.keys():
        # update value @id with the path in server of the manifest.json
        dict_image = {"@context": "http://iiif.io/api/image/2/context.json", "@id": filename, "@type": "sc:Manifest",
                      "label": filename, "sequences": [{"canvases": []}]}
        images = manifest["images"]

        for k, v in images.items():
            try:
                data_image = open_data(v)
            except Exception as E:
                print("Impossible to access at the IIIF image server for "+filename, E)
                continue
            dict_service = {i: data_image[i] for i in data_image if i != 'height' and i != 'width' and i != 'sizes'}
            image = {"@id": data_image["@id"],
                   "label": k,
                   "height": data_image["height"],
                   "width": data_image["width"],
                   "images": [
                       {"resource":{
                        "@id": data_image["@id"] + "/full/full/0/default.jpg",
                        "service": dict_service,
                        "height": data_image["height"],
                        "width": data_image["width"]
                        },
                        "on": data_image["@id"]
                       }
                   ],
                    "related": ""}
            dict_image["sequences"][0]["canvases"].append(image)
        return dict_image
    else:
        url = manifest["manifest_link"]
        try:
            data = open_data(url)
        except:
            print("The " + filename + " don't work")
            return False
        if "images" in manifest.keys():
            images = manifest["images"]
            canvases = []
            for k, v in images.items():
                for sequence in data["sequences"]:
                    for canvase in sequence["canvases"]:
                        if v == canvase["@id"]:
                            canvase["label"] = k
                            canvases.append(canvase)
            for sequence in data["sequences"]:
                del sequence["canvases"]
                sequence["canvases"] = canvases
            return data
        else:
            return data


def open_data(url):
    try:
        r = requests.get(url)
    except requests.exceptions.SSLError as E:
        print(E)
        r = requests.get(url, verify=False)
    return r.json()


def cmd():
    create_mapping(sys.argv[1])


if __name__ == '__main__':
    cmd()
