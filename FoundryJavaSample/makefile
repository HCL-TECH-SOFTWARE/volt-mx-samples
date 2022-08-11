SHELL = /usr/bin/env bash

#############################################################################################
# IMPORTANT: Run 'make conf-git-filters' before adding your user and password to this file. #
#############################################################################################

foundry_dir=foundry
foundry_proj=HelloWorld

java_dir=java
java_proj=HelloWorld

# Compile the Java assets, copy them into the Foundry app and zip it up.
build: clean javac copy zip
	printf "\nDone!\nNow import $(foundry_proj).zip into Foundry.\n\n"

# Run Maven clean and remove all .jar and .zip files from this directory.
clean:
	find $(foundry_dir) -name '*.jar' -delete
	cd $(java_dir)/$(java_proj) && mvn clean
	find . -name '*.zip' -delete

# Compile the Java assets.
javac:
	cd $(java_dir)/$(java_proj) && mvn package

# Copy the JAR files built into the Foundry app's directory.
copy:
	cp $(java_dir)/$(java_proj)/target/*.jar $(foundry_dir)/$(foundry_proj)/Apps/_JARs/

# Zip up the Foundry app for import/upload.
zip:
	cd $(foundry_dir)/$(foundry_proj) && zip --recurse-paths --display-bytes ../../$(foundry_proj).zip * --exclude \*.DS_Store \*thumbs.db \*.desktop.ini

# Avoid pushing your Foundry password to source control.
conf-git-filters:
	git config --global filter.foundry_makefile.clean 'sed -e "s/\(.*foundry_acct.*=\).*/\1/g; s/\(.*foundry_user.*=\).*/\1/g; s/\(.*foundry_pssw.*=

# Note: Set these three as environment variables so that switching branches won't blank them.
# The 9 digit Foundry account ID —e.g.: 100000001
foundry_acct=
# The developer's user for the Foundry Console —e.g.: jimi.hendrix@purple.com
foundry_user=
# The developer's password for the Foundry Console.
foundry_pssw=

show:
	printf "acct: %s\nuser: %s\npssw: %s\n" $(foundry_acct) $(foundry_user) $(foundry_pssw)

# Export/download the Foundry app from the Foundry Console and decompress it to the local file system.
export:
	rm -f $(foundry_proj).zip
	foundry export --account $(foundry_acct) --user $(foundry_user) --password $(foundry_pssw) --app $(foundry_proj) --file $(foundry_proj).zip
	rm -rf foundry/$(foundry_proj)
	unzip $(foundry_proj).zip -d foundry/$(foundry_proj)
	rm $(foundry_proj).zip

# Import/upload the already compressed Foundry app into the Foundry Console.
import:
	foundry import --account $(foundry_acct) --user $(foundry_user) --password $(foundry_pssw) --file $(foundry_proj).zip
