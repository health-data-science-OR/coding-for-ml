FROM ubuntu:20.04

#install wget
RUN apt-get update \
  && apt-get install -y wget \
  && rm -rf /var/lib/apt/lists/*

#get the latest version of miniconda
RUN wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh

# install in batch (silent) mode, does not edit PATH or .bashrc or .bash_profile
# -p path
# -f force
RUN bash Miniconda3-latest-Linux-x86_64.sh -b

ENV PATH=/root/miniconda3/bin:${PATH} 

# cleanup
RUN rm Miniconda3-latest-Linux-x86_64.sh

#update conda 
RUN conda update -y conda

#create directory for code.
RUN mkdir /home/code

#set working directory.
WORKDIR /home/code

# Copy all files across to container
COPY . /home/code

# Install anaconda, conda-forge and pip dependencies the clean up.
RUN conda env create -f binder/environment.yml && conda clean -afy

#open a port
EXPOSE 80
