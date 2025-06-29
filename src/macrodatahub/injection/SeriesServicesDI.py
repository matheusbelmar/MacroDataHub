# catalog/registry.py
import importlib

SCRAPER_REGISTRY = {
    "ibge": {"scraper": ("macrodatahub.adapters.outbound.sources.ibge.ibge_scraper", "IBGEScraper"),
             "cleaner": ("macrodatahub.adapters.outbound.sources.ibge.ibge_cleaner", "IBGEScleaner")},
    "sgs":  {"scraper": ("macrodatahub.adapters.outbound.sources.sgs.sgs_scraper", "SGSscraper"),
             "cleaner": ("macrodatahub.adapters.outbound.sources.sgs.sgs_cleaner", "SGScleaner")}
}

def get_component(source: str, component_type: str):
    
    coords=SCRAPER_REGISTRY[source][component_type]
    try:
        module_path, class_name = coords[0],coords[1]
    except KeyError:
        raise ValueError(f"Component '{component_type}' for source '{source}' not found.")

    module = importlib.import_module(module_path)
    cls = getattr(module, class_name)
    return cls