use strict;
use warnings;
use Bio::PrimarySeqI;
use lib 'C:\Users\anjal\OneDrive\Desktop\src\ensembl\modules';
use Bio::EnsEMBL::Registry;
use Bio::EnsEMBL::DBSQL::SliceAdaptor

my $registry = 'Bio::EnsEMBL::Registry';
$registry->load_registry_from_db(
    -host   => 'ensembldb.ensembl.org',
    -user   => 'anonymous',
    
);

# get the SliceAdaptor and Slice
my $slice_adaptor = $registry->get_adaptor('Homo sapiens', 'Core', 'Slice');
my $slice = $slice_adaptor->fetch_by_region('chromosome', 1, 54_960_000, 54_980_000);