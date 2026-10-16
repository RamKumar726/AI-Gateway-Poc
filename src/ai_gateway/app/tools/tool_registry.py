from .product_tools import search_products, get_product_details
import logging

logging.basicConfig(level=logging.INFO)

TOOL_REGISTRY = {
    "search_products" : search_products,
    "get_product_details" : get_product_details
}

def load_tool(tool_names) :
    selected_tools = []
    for tool_name in tool_names:
        tool = TOOL_REGISTRY.get(tool_name)
        logging.info(f"loaded tool {tool.name}")
        if tool is None:
            raise ValueError(f"No tool found with name {tool_name}")
        selected_tools.append(tool)

    return selected_tools


            
