def tag(name, *content, cls = None, **attrs):

    """generate one or couple of HTML tags"""

    if cls is not None:
        attrs["class"] = cls

    if attrs:
        attrs_str = "".join(f"{attr}='{value}'" for attr, value in sorted(attrs.items()))

    else:
        attrs_str = ""
    if content:
        return "\n".join(f"<{name} {attrs_str}>{c}</{name}" for c in content)        

    else:
        return "".join(f"<{name}{attrs_str}/>")    


print(tag("p", "hello"))        