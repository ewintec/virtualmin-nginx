#!/usr/bin/perl
# Show location URL rewrite options

use strict;
use warnings;
require 'virtualmin-nginx-lib.pl';
our (%text, %in, %rewrite);
&ReadParse();
my $server = &find_server($in{'id'});
$server || &error($text{'server_egone'});
&can_edit_server($server) || &error($text{'server_ecannot'});
my $location = &find_location($server, $in{'path'});
$location || &error($text{'location_egone'});

&ui_print_header(&location_desc($server, $location),
		 $text{'rewrite_title'}, "");

print &ui_form_start("save_lrewrite.cgi", "post");
print &ui_hidden("id", $in{'id'});
print &ui_hidden("path", $in{'path'});
print &ui_table_start($text{'rewrite_header'}, undef, 2);

print &nginx_rewrite_input("rewrite", $location);

print &nginx_onoff_input("rewrite_log", $location);

print &ui_table_end();
print &ui_form_end([ [ undef, $text{'save'} ] ]);

&ui_print_footer("edit_location.cgi?id=".&urlize($in{'id'}).
		   "&path=".&urlize($in{'path'}),
		 $text{'location_return'},
		 "edit_server.cgi?id=".&urlize($in{'id'}),
		 $text{'server_return'});
