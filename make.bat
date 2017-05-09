@echooff
md ..\build_gh-pages
md ..\build_gh-pages\static
md ..\build_gh-pages\images
md ..\build_gh-pages\code
copy static\*.* ..\build_gh-pages\static
copy images\*.* ..\build_gh-pages\images
copy code\*.* ..\build_gh-pages\code
cd zh_CN
parm make -d ..\..\build_gh-pages\zh_CN
cd ..\en
parm make -d ..\..\build_gh-pages\en
cd ..
copy /Y index.html ..\build_gh-pages\
