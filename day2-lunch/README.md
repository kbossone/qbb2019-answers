QUESTION 1:
First 10,000 reads in fastq file and word count:

	/Users/cmdb/qbb2019-answers $ head -n 40000 day2-lunch/SRR072893.fastq > day2-lunch/first10kSRR072893.fastq
	/Users/cmdb/qbb2019-answers $ wc
	
Quality report:
	
	/Users/cmdb/qbb2019-answers/day2-lunch $ fastqc first10kSRR072893.fastq 
	/Users/cmdb/qbb2019-answers/day2-lunch $ ls
	/Users/cmdb/qbb2019-answers/day2-lunch $ open first10kSRR072893_fastqc.html

Map reads to BDGP6:
	
	/Users/cmdb/qbb2019-answers/day2-lunch $ hisat2 -p 4 -x BDGP6 -U first10kSRR072893.fastq -S SRR072893-10k.sam

convert and index
	
	/Users/cmdb/qbb2019-answers/day2-lunch $ samtools sort -@ 4 SRR072893-10k.sam -o indexed-SRR072893-10k.bam
	/Users/cmdb/qbb2019-answers/day2-lunch $ samtools index indexed-SRR072893-10k.bam indexed-SRR072893-10k.bam.bai

Quantify:
	
	/Users/cmdb/qbb2019-answers/day2-lunch $ stringtie indexed-SRR072893-10k.bam -G BDGP6.Ensembl.81.gtf -o quant.SRR072893-10k.gtf -p 4 -e -B
	
QUESTION 3:

	/Users/cmdb/qbb2019-answers/day2-lunch $ cut -f 3 SRR072893.sam | grep -v "LN" "*" | sort -n | uniq -c
grep "^SRR072893" SRR072893.sam |cut -f 3 | sort | uniq -c


Another hella better way is with python.