Vagrant.configure("2") do |config|
    config.vm.define "centos" do |jh|
        config.vm.provider "virtualbox" do |v|
            v.memory = 4096
            v.cpus = 2
    end
    jh.vm.host_name = "node01"
    jh.vm.network  "private_network", ip: "192.168.59.221"
    jh.vm.box = "generic/ubuntu2204"
    jh.vm.synced_folder "./voiceclone", "/voiceclone"
    # jh.disksize.size='20GB'
    end
end