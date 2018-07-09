#!/usr/bin/env python

import re
import hashlib
import json
from pprint import pprint as p
class KindleNote():

    NoteData = {}
    expend_list = []
    filename = ""


    def __init__(self,filename):
        self.filename = filename

    def file_format(self):
        with open(self.filename,'rt') as f:
            note = []
            for line in f:
                if line == "="*10+"\n":
                    self.note_format(note)
                    note = []
                else:
                    note.append(line)
        for n in self.expend_list:
            self.add_note(n)
        return self


    def note_format(self,data):
        """ format note to json string"""
        json_note = {}
        json_note["name"] = data[0]
        json_note["content"] = data[3]

        (json_note["start"],json_note["end"]) = self.get_postion(data[1])
        json_note["createtime"] = self.get_create_time(data[1])

        if "标注" in data[1]:
            self.add_mark(json_note)
        elif "笔记" in data[1]:
            self.add_note(json_note)
        return

    def add_mark(self,data):
        """add mark as top into json struct"""
        name_md5 = hashlib.md5(data["name"].encode(encoding='utf-8')).hexdigest()
        if name_md5 not in self.NoteData:
            self.NoteData[name_md5] = []
        self.NoteData[name_md5].append(data)
        return

    def add_note(self,data):
        """add note to mark"""
        name_md5 = hashlib.md5(data["name"].encode(encoding='utf-8')).hexdigest()
        if name_md5 not in self.NoteData:
            self.expend_list.append(data)
        else:
            for n in range(len(self.NoteData[name_md5])):
                note = self.NoteData[name_md5][n]
                if data["start"] == note["start"] or data["start"] == note["end"]:
                    self.NoteData[name_md5][n]["note"] = data

    def get_postion(self,data):
        """ get note's postion on book"""
        pos_reg = re.compile(r'(.*\s#?(\d+)-(\d+).*\|.*|.*\s#?(\d+).*\|.*)')
        pos_list = pos_reg.match(data).groups()

        if pos_list != None:
            if pos_list[3] == None:
                return (pos_list[1],pos_list[2])
            else:
                return (pos_list[3],"")
        else:
            return ("","")
        
    def get_create_time(self,data):
        """ get time when have a note on the book"""
        t_list = data.split(" ")
        if len(t_list) == 8:
            return t_list[6] + t_list[7]
        else:
            return t_list[5] + t_list[6]


    def save_as_json(self):
        with open("./data.json","wt") as f:
            json.dump(self.NoteData,f)
            print("保存成功")

    def load_json_file(self):
        with open("./data.json","rt") as f:
            p(json.load(f))

if __name__ == "__main__":
    kindle_notes = KindleNote("clippings.txt")
    
    kindle_notes.file_format().save_as_json()

    kindle_notes.load_json_file()
    
