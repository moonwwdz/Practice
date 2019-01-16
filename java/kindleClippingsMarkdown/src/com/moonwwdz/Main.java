package com.moonwwdz;

import java.io.*;
import java.nio.charset.StandardCharsets;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.*;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import java.util.stream.Collectors;

public class Main {

    public static String filePath = "H:\\clippings.txt";

    public static void main(String[] args) {
        ClippingCont clippingCont = new ClippingCont();
        List<ClippingCont> conts = new ArrayList<>();
        try {
            BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(new FileInputStream(filePath), StandardCharsets.UTF_8));

            String tempString;
            while ((tempString=bufferedReader.readLine()) != null) {
                //分隔每条笔记
                if (tempString.startsWith("==========")) {
                    conts.add(clippingCont);
                    clippingCont = new ClippingCont();
                    continue;
                }

                if(null == tempString || "" == tempString){
                    continue;
                } else if (clippingCont.getName() == null) {
                    //取笔记中书名作者信息
                    Pattern namePattern = Pattern.compile("(^.*?\\s)\\((.*?)\\)$");
                    Matcher matcher = namePattern.matcher(tempString);
                    if (matcher.find()) {
                        clippingCont.setName(matcher.group(1));
                        clippingCont.setAuthor(matcher.group(2));
//                        System.out.println(matcher.group(1) + "---" + matcher.group(2));
                    }else {
                        clippingCont.setName(tempString);
                        clippingCont.setAuthor("");
                    }
                } else if (clippingCont.getType() == null) {
                    //取类型及位置
                    Pattern typePattern = Pattern.compile("^.*?(\\d+-\\d+|\\d+).*?的(.*?)\\s\\|\\s添加于\\s(\\d+年\\d+月\\d+日)(.*)\\s(.*)(\\d+:\\d+:\\d+)$");
                    Matcher matcher = typePattern.matcher(tempString);
                    if (matcher.find()) {
                        clippingCont.setPos(matcher.group(1));
                        clippingCont.setType(matcher.group(2).equals("笔记") ? 1 : 2);
                        clippingCont.setWeek(matcher.group(4));

                        SimpleDateFormat sdf =  new SimpleDateFormat( "yyyy年MM月dd日 hh:mm:ss" );
                        String timeH = matcher.group(6);
                        if (timeH.length() < 8) {
                            timeH = "0" + timeH;
                        }
                        Date date = sdf.parse(matcher.group(3) + " " + timeH);

                        if ("下午".equals(matcher.group(5))) {
                            Calendar calendar = Calendar.getInstance();
                            calendar.setTime(date);
                            calendar.add(Calendar.HOUR,12);
                            date = calendar.getTime();
                        }
                        SimpleDateFormat sdfEnd = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss");
                        clippingCont.setTime(sdfEnd.format(date));
                    }
                } else {
                    clippingCont.setContent(null == clippingCont.getContent() ? "" : clippingCont.getContent() + tempString);
                }
            }
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        } catch (ParseException e) {
            e.printStackTrace();
        }


        Map<String,List<ClippingCont>> mapClips = conts.stream().collect(Collectors.groupingBy(ClippingCont::getName));
        mapClips.forEach((k,notes)->{
            List<ClippingCont> commitList = notes.stream().filter(v -> v.getType().equals(1)).collect(Collectors.toList());
            List<ClippingCont> noteList = notes.stream().filter(v -> v.getType().equals(2)).collect(Collectors.toList());
            commitList.forEach(commit->{
                noteList.forEach(origin->{
                    if (origin.getPos().trim().contains(commit.getPos().trim()) || commit.getPos().trim().contains(origin.getPos().trim())) {
                        origin.setCommit(commit.getContent());
                    }
                });
            });
        });

        //System.out.println("Finish init data");

        File mdFile = new File("notes.md");
        try {
            mdFile.createNewFile();
            BufferedWriter mdWrite = new BufferedWriter(new FileWriter(mdFile));
            mapClips.forEach((name,values)->{
                List<ClippingCont> exceptCommit = values.stream().filter(v -> v.getType().equals(2)).collect(Collectors.toList());;
                try {
                    mdWrite.write("## " + markdownStr(name));
                    for (Integer i = 0; i < exceptCommit.size(); i++) {
                        ClippingCont temp = exceptCommit.get(i);
                        if (i.equals(0)) {
                            mdWrite.write(markdownStr("*" + temp.getAuthor() + "*"));
                        }
                        mdWrite.write(markdownStr("> " + temp.getContent()));
                        if (null != temp.getCommit() && "" != temp.getCommit()) {
                            mdWrite.write(markdownStr(temp.getCommit()));
                        }
                    }
                    mdWrite.write(markdownStr("------"));
                } catch (IOException e) {
                    e.printStackTrace();
                }
            });
            mdWrite.flush();
            mdWrite.close();
        } catch (IOException e) {
            e.printStackTrace();
        }


    }

    public static String markdownStr(String s) {
        return s + "\n\n";
    }
}
