import wikipediaapi
import time

def DFS(start_article, target_article):
    """
    Finds the shortest path using Depth First Search
    """
    path = {}
    path[start_article] = [start_article]
    counter = 0
    fringe = [start_article]

    while len(fringe) != 0:
        parent_page = fringe.pop()
        backlinks = get_backlinks(parent_page)
        print(len(fringe))
        for page in backlinks:
            if page == target_article:
                return path[parent_page] + [page], counter

            if page not in path:
                if page != parent_page:
                    path[page] = path[parent_page] + [page]
                    counter += 1
                    print("-->".join(path[page]))
                    fringe.append(page)
    return None

def BFS(start_article, target_article):
    """
    Finds the shortest path using Breadth First Search
    """
    path = {}
    path[start_article] = [start_article]
    counter = 0
    fringe = [start_article]

    while len(fringe) != 0:
        parent_page = fringe.pop(0)
        backlinks = get_backlinks(parent_page)
        print(len(fringe))
        for page in backlinks:
            if page == target_article:
                return path[parent_page] + [page], counter

            if page not in path:
                if page != parent_page:
                    path[page] = path[parent_page] + [page]
                    counter += 1
                    print("-->".join(path[page]))
                    fringe.append(page)
    return counter

def UCS(start_article, target_article):
    """
    Finds the shortest path using Breadth First Search
    """
    path = {}
    path[start_article] = [start_article]
    counter = 0
    fringe = [start_article]
    print(fringe)
    while len(fringe) != 0:
        parent_page = fringe.pop(0)
        backlinks = get_backlinks(parent_page)
        #print(len(fringe))
        for page in backlinks:
            if page == target_article:
                return path[parent_page] + [page], counter

            if page not in path:
                if page != parent_page:
                    path[page] = path[parent_page] + [page]
                    counter += 1
                    #print("-->".join(path[page]))
                    fringe.append(page)
    return counter

def get_backlinks(article_name):
    """
    Gets the backlinks of a given page
    """
    article_page = wiki.page(article_name)
    filtered = [article for article in article_page.links.keys() if not article.startswith("Module:") \
                                                                and not article.startswith("Portal:") \
                                                                and not article.startswith("Category:") \
                                                                and not article.startswith("Help:") \
                                                                and not article.startswith("Template") \
                                                                and not article.startswith("File:") \
                                                                and not article.startswith("Wikipedia") \
                                                                and not article.startswith("Talk:")
                                                                ]
    return filtered


if __name__ == "__main__":
    wiki = wikipediaapi.Wikipedia('en')

    start_time = time.time()

    start_article = "Rammstein"
    target_article = "King Gizzard and the Lizard Wizard"
    found_path, counter = UCS(start_article, target_article)
    print("\n\n\n" + "-->".join(found_path))
    end_time = time.time()
    total_time = end_time - start_time
    print(f"Total time: {total_time}")
    print(f"Nmber of operations: {counter}")