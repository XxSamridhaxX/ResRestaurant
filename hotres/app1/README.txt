starting dekhi first samma kasari use garne

#paila herne kun branch using:
    git branch

        #yo chai bhairakheko branch use garna:
        git checkout <branch-name>  (branch-name ma branch ko name lekhne)  

        #naya branch banauna:
        git checkout -b <branch-name>  (branch-name ma branch ko name lekhne)

        #file ra code change garepaxi:
        git add <file-name>  (file-name ma file ko name lekhne)
          # if sabai changes pathaune bhaye chai:
          git add .

        #commit garna:
        git commit -m "<commit-message>"  (commit-message ma commit message lekhne)
        
        Note: commit garepxi afno device ma matrai commit bhayera basxa, push garnu agadi changes correct xa ki xaina sure garne

        aba goto line no 26



#git push to branch:
    git push origin <branch-name>  (branch-name ma branch ko name lekhne)

    #git push to master:
    git push origin master



#git pull garna:
    git pull origin <branch-name>  (branch-name ma branch ko name lekhne)

    #git pull from main:
    git pull origin master




Process for pushing:

git add . 
git checkout branch-name 
git commit -m "first commit"
git push origin branch-name



Process for pulling 
git pull origin branch-name / git pull master