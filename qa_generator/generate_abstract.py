import os
from chat_with_model import chat_with_model


def generate_abstract(
        llm_url, llm_token, llm_method, text_chunk, text_wrap, content_dir, paragraphs):
    if len(paragraphs) == 0:
        return ''
    try:
        with open(os.path.join(content_dir, 'op_para_abstract_content.txt'), 'r') as f:
            op_para_abstract_content = f.read()
    except:
        print("读取文档摘要生成content失败")
        exit()
    pre_abstract = paragraphs
    pre_range = []
    for i in range(len(pre_abstract)):
        pre_range.append([i, i])
    nex_abstact = []
    nex_range = []
    while len(pre_abstract) > 1:
        index = 0
        nex_abstact = []
        nex_range = []
        while index < len(pre_abstract):
            if index == len(pre_abstract)-1:
                nex_abstact.append(pre_abstract[index])
                nex_range.append(pre_range[index])
                index += 1
                continue
            abstract1 = pre_abstract[index]
            abstract2 = pre_abstract[index+1]
            st = max(0, pre_range[index][1]-text_wrap+1)
            en = min(len(paragraphs)-1, pre_range[index+1][0]+text_wrap-1)
            link_text = ''.join(paragraphs[st:en+1])
            content = op_para_abstract_content.format(
                text_chunk=text_chunk, abstract1=abstract1, link_text=link_text, abstract2=abstract2)
            for i in range(10):
                abstract = chat_with_model(llm_url, llm_token, llm_method, content, '请输出一个优化过的摘要')
                if len(abstract) <= text_chunk:
                    break
            nex_abstact.append(abstract)
            nex_range.append([pre_range[index][0], pre_range[index+1][1]])
            index += 2
        pre_abstract = nex_abstact[:]
        pre_range = nex_range[:]
    abstract = pre_abstract[0]
    return abstract
