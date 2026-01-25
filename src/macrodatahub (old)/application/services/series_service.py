# application/services/series_service.py

#from macrodatahub.domain.ports.scraper_port import ScraperPort
#from macrodatahub.domain.ports.storage_port import StoragePort
#from macrodatahub.domain.ports.format_port import FormatPort
#from macrodatahub.catalog.registry import Catalog
#from macrodatahub.domain.models.series import Series

from typing import Union, List
from macrodatahub.injection.SeriesServicesDI import get_component

class SeriesService:
    def __init__(
            self
#            formatter: FormatPort
#            catalog: Catalog
            ):
#        self.formatter = formatter
#       self.catalog = catalog
        pass


    def download(
        self,
        Series_name: Union[str, List[str]],
        code    : str,
        source  : str,
        path    : str  = None,
        clean   : bool = True,
        storage : bool = True,
        register: bool = False
    ):
        
        Saving_path=r"data/raw_storage/Not_Registered/{}/{}".format(Series_name, code)
        ScraperCls=get_component(source=source, component_type="scraper")
        scraper = ScraperCls(code=code, path=Saving_path)
        scraper.Scrap()

        return 


    def load(
        self,
        series_name: str,
        clean: bool = True
    ):
        pass

    def upload(
        self,
        series_name: str
    ):
        pass